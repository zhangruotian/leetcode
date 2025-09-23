# X(B,L,D)
import torch.nn as nn
import torch
import torch.nn.functional as F 
class SelfAttention(nn.Module):
    def __init__(self,D,num_heads):
        super().__init__()
        self.D = D 
        self.wqkv = nn.Linear(self.D,self.D*3)
        self.num_heads = num_heads
        self.head_d = self.D//self.num_heads
        self.scale = self.head_d**-0.5
        self.proj = nn.Linear(self.D,self.D)

    def forward(self,X):
        B,L,_ = X.shape #X(B,L,D)
        qkv = self.wqkv(X) #X(B,L,3D)
        qkv = qkv.view(B,L,3,self.num_heads,self.head_d) #qkv(B,L,3,#heads,head_d)
        q,k,v = qkv.unbind(2) # q,k,v(B,L,#heads,head_d)
        q,k,v = [t.transpose(1,2) for t in (q,k,v)] #q,k,v(B,#heads,L,head_d)
        attn = q@k.transpose(-1,-2)*self.scale # attn (B,#heads,L,L)
        mask = torch.triu(torch.ones((L,L),dtype=torch.bool,device=X.device),1)
        attn = attn.masked_fill(mask,-1e9)
        score = F.softmax(attn,-1) # score (B,#heads,L,L)
        out = score@v # attn (B,#heads,L,head_d)
        out = out.transpose(1,2).reshape(B,L,self.D)
        return self.proj(out)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)
model = SelfAttention(1024, 8).to(device)
X = torch.rand(16, 512, 1024).to(device)
print(model(X))

