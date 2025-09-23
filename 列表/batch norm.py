import numpy as np

class BatchNorm:

    def __init__(self, C, momentum=0.9, eps=1e-5):
        self.gamma = np.ones((1, C, 1, 1))
        self.beta = np.zeros((1, C, 1, 1))

        self.ema_mean = np.zeros((1, C, 1, 1))
        self.ema_var = np.ones((1, C, 1, 1))

        self.momentum = momentum
        self.eps = eps
        self.train_mode = True

    def forward(self, X):
        # X shape: (B, C, H, W)
        
        if self.train_mode:
            # 直接使用 np.var，代码最简洁且不易出错
            mean = np.mean(X, axis=(0, 2, 3), keepdims=True)
            var = np.var(X, axis=(0, 2, 3), keepdims=True)

            self.ema_mean = self.momentum * self.ema_mean + (1 - self.momentum) * mean
            self.ema_var = self.momentum * self.ema_var + (1 - self.momentum) * var
        else:
            mean = self.ema_mean
            var = self.ema_var

        # 标准化 (X 和 mean/var 的形状可以直接广播)
        X_normalized = (X - mean) / np.sqrt(var + self.eps)

        # 缩放和平移
        out = self.gamma * X_normalized + self.beta
        
        return out

    def train(self):
        self.train_mode = True

    def eval(self):
        self.train_mode = False

bn = BatchNorm(C=32)
# x: (4,32,16,16)
x = np.random.normal(0, 1, (4,32,16,16))
x_norm = bn.forward(x)
print(x_norm.shape)
