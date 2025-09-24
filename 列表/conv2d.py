import numpy as np

class Conv2d:

    def __init__(self,kh,kw,c_in,c_out,padding,stride_h,stride_w):
        self.kernel = np.random.randn(c_out,c_in,kh,kw) #(c_out,c_in,kh,kw)
        self.b = np.random.randn(c_out,1,1)
        self.padding=padding
        self.stride_h = stride_h
        self.stride_w = stride_w 

    def forward(self,X):
        # X(B,C,H,W)
        X = np.pad(X,((0,0),(0,0),(self.padding,self.padding),(self.padding,self.padding)))
        B,C,H,W = X.shape
        c_out,c_in,kh,kw = self.kernel.shape
        h_out = (H-kh)//self.stride_h+1
        w_out = (W-kw)//self.stride_w+1
        out = np.zeros((B,c_out,h_out,w_out))

        for b in range(B):
            x = X[b]#(C,H,W)
            for c in range(c_out):
                kernel = self.kernel[c] #(C,kh,kw)
                for i in range(h_out):
                    for j in range(w_out):
                        out[b,c,i,j]=np.sum(x[:,i*self.stride_h:i*self.stride_h+kh,j*self.stride_w:j*self.stride_w+kw]*kernel)
        out += self.b
        return out 

if __name__=='__main__':
    model = Conv2d(2,2,2,2,0,2,2)
    X = np.ones((2,2,4,4))
    res = model.forward(X)
    print(res)
