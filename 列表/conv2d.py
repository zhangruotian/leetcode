import numpy as np

def conv2d(x, w, bias, stride, padding):
    # x: (N, Cin, H, W)
    # w: (Cout, Cin, kH, kW)
    # bias: (Cout,) 或 None
    # stride: (sH, sW)      padding: (pH, pW)
    N, Cin, H, W = x.shape
    Cout, _, kH, kW = w.shape
    sH, sW = stride
    pH, pW = padding

    # zero padding
    xp = np.pad(x, ((0,0),(0,0),(pH,pH),(pW,pW)))
    Hp, Wp = xp.shape[2], xp.shape[3]

    # 输出尺寸
    Hout = (Hp - kH) // sH + 1
    Wout = (Wp - kW) // sW + 1
    y = np.zeros((N, Cout, Hout, Wout), dtype=x.dtype)

    for n in range(N):
        for co in range(Cout):
            for i in range(Hout):
                h0 = i * sH
                h1 = h0 + kH
                for j in range(Wout):
                    w0 = j * sW
                    w1 = w0 + kW
            
                    # 1. 提取感受野 (Extract the receptive field)
                    image_patch = xp[n, :, h0:h1, w0:w1]
                    
                    # 2. 提取当前卷积核 (Extract the current filter)
                    current_filter = w[co]
                    
                    # 3. 逐元素相乘并求和 (Element-wise multiply and sum)
                    y[n, co, i, j] = np.sum(image_patch * current_filter)
            
            # 将偏置项加到整个通道上
            if bias is not None:
                y[n, co] += bias[co]
                
    return y

x=np.ones((1,2,2,2))
w = np.ones((2,2,2,2))
bias = np.zeros((2,1))
stride = (1,1)
padding = (0,0)

print(conv2d(x,w,bias,stride,padding))

