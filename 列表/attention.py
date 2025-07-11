import torch

class MultiHeadAttention(nn.Module):

    def __init__(self,embed_dim,num_heads):
        super().__init__()
        assert embed_dim % num_heads == 0

        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        self.scale = self.head_dim ** -0.5

        self.w_qkv = nn.Linear(embed_dim, embed_dim * 3)
        self.out_proj   = nn.Linear(embed_dim, embed_dim)


    def forward(self,x):
        # x(B,L,D)
        B,L,_=x.shape
        qkv = self.w_qkv(x) # B,L,3D
        qkv = qkv.reshape(B, L, 3, self.num_heads, self.head_dim)  #B,L,3,H,HD
        q,k,v = qkv.unbind(dim=2) # q (B,L,H,HD)
        q, k, v = [t.transpose(1, 2) for t in (q, k, v)]   # q (B,H,L,HD)

        attn_scores = torch.matmul(q, k.transpose(-2, -1)) * self.scale   # (B, H, L, L)
        causal_mask = torch.triu(torch.ones(L, L), diagonal=1)
        attn_scores = attn_scores.masked_fill(causal_mask, -1e9) # 将需要屏蔽的位置填充为负无穷
        attn_probs  = F.softmax(attn_scores, dim=-1)
        context = torch.matmul(attn_probs, v)  # (B, H, L, d_k) 
        context = context.transpose(1, 2).reshape(B, L, self.embed_dim)  # (B, L, D)

        out = self.out_proj(context)
        return out, attn_probs
        






