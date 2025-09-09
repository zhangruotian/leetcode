import numpy as np

class BatchNorm2d:
    def __init__(self, C, eps=1e-5, momentum=0.1):
        self.eps = eps
        self.momentum = momentum

        # learnable params (broadcast 成 (1,C,1,1))
        self.gamma = np.ones((1, C, 1, 1), dtype=np.float32) 
        self.beta  = np.zeros((1, C, 1, 1), dtype=np.float32)

        # running stats for inference（按通道）
        self.running_mean = np.zeros((1, C, 1, 1), dtype=np.float32)
        self.running_var  = np.ones((1, C, 1, 1), dtype=np.float32)

    def forward(self, x, training=True):
        """
        x: (N, C, H, W)
        """
        if training:
            # 按通道在 (N,H,W) 上做均值/方差
            mean = x.mean(axis=(0, 2, 3), keepdims=True)                # (1,C,1,1)
            var  = ((x - mean) ** 2).mean(axis=(0, 2, 3), keepdims=True)  # (1,C,1,1)

            # 标准化
            x_hat = (x - mean) / np.sqrt(var + self.eps)

            # 更新运行均值/方差（EMA）
            m = self.momentum
            self.running_mean = (1 - m) * self.running_mean + m * mean
            self.running_var  = (1 - m) * self.running_var  + m * var
        else:
            # 推理：使用运行统计量（冻结）
            x_hat = (x - self.running_mean) / np.sqrt(self.running_var + self.eps)

        # 仿射变换（恢复表达能力）
        return self.gamma * x_hat + self.beta

bn = BatchNorm2d(C=32)
# x: (4,32,16,16)
x = np.random.normal(0, 1, (4,32,16,16))
x_norm = bn.forward(x)
print(x_norm.shape)
