import numpy as np 

class Conv2d:
    def __init__(self,cin,cout,kh,kw):
        self.cin = cin
        self.cout = cout
        self.kh = kh
        self.kw = kw
        self.weights = np.random.randn(cout,cin,kh,kw) #(cout,cin,kh,kw)
        self.bias = np.random.randn(cout)

    def forward(self,X,padding,stride):
        X = np.pad(X,((0, 0), (0, 0), (padding, padding), (padding, padding))) # X(B,cin,H,W)
        B,cin,H,W = X.shape
        X_out_h = (H-self.kh)//stride+1
        X_out_w = (W-self.kw)//stride+1
        X_out = np.zeros((B,self.cout,X_out_h,X_out_w))
        for b in range(B):
            x = X[b] #(cin,H,W)
            for c in range(self.cout):
                weight = self.weights[c] #(cin,kh,kw)
                bias = self.bias[c] #(1)
                for i in range(X_out_h):
                    h_top = i*stride
                    h_bot = h_top+self.kh
                    for j in range(X_out_w):
                        w_left = j*stride
                        w_right = w_left+self.kw
                        X_out[b,c,i,j] = np.sum(x[:,h_top:h_bot,w_left:w_right]*weight)+bias
        return X_out

if __name__ == '__main__':
    X = np.ones((2,2,4,4))
    model = Conv2d(2,1,2,2)
    model.weights = np.ones((1,2,2,2))
    model.bias = np.ones(1)
    res = model.forward(X,0,2)
    expected = np.full((2,1,2,2),9)
    print(np.all(res==expected))
