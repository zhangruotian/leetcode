import torch
import torch.nn.functional as F
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self,num_heads,D):
        super().__init__()
        self.num_heads = num_heads
        self.D = D 
        self.qkv_w = nn.Linear(D,3*D)
        self.head_D = self.D//self.num_heads
        self.scale = self.head_D ** -0.5
        self.out_proj = nn.Linear(D,D)

    def forward(self,x):
        # x(B,L,D)
        B,L,_ = x.shape
        qkv = self.qkv_w(x) # (B,L,3D)
        qkv = qkv.view(B,L,3,self.num_heads,self.head_D)
        q,k,v = qkv.unbind(2) # (B,L,num_heads,hD)
        q,k,v = [m.transpose(1,2) for m in (q,k,v)] # (B,num_heads,L,hD)

        attn = torch.matmul(q,k.transpose(-1,-2))*self.scale #(B,num_heads,L,L)
        mask = torch.triu(torch.ones((L,L),dtype=torch.bool),1) 
        attn = attn.masked_fill(mask,-1e9)
        score = F.softmax(attn,-1) # #(B,num_heads,L,L)
        print(score)
        out = torch.matmul(score,v).transpose(1,2).reshape(B,L,self.D) #(B,num_heads,L,hD)
        return self.out_proj(out)

model = MultiHeadAttention(2,4)
x = torch.rand(4,2,4)
print(model(x))

