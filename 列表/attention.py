import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, D, num_heads, attn_drop):
        super().__init__()
        assert D % num_heads == 0, "D must be divisible by num_heads"
        self.wqkv = nn.Linear(D, 3 * D)
        self.proj = nn.Linear(D, D)
        self.num_heads = num_heads
        self.head_d = D // num_heads
        self.scale = self.head_d ** -0.5
        self.attn_drop = nn.Dropout(attn_drop)

    def forward(self, X):
        B, L, D = X.shape
        qkv = self.wqkv(X)
        qkv = qkv.view(B, L, 3, self.num_heads, self.head_d)
        q, k, v = qkv.unbind(2)
        q, k, v = [t.transpose(1, 2) for t in (q, k, v)]
        attn = (q @ k.transpose(-1, -2)) * self.scale
        mask = torch.triu(torch.ones((L, L), device=X.device, dtype=torch.bool), diagonal=1)
        attn = attn.masked_fill(mask, float('-inf'))
        score = F.softmax(attn, dim=-1)
        score = self.attn_drop(score)
        out = score @ v
        out = out.transpose(1, 2).contiguous().view(B, L, D)
        return self.proj(out)

class AttentionBlock(nn.Module):
    def __init__(self, D, num_heads, attn_drop, proj_drop):
        super().__init__()
        self.attn = MultiHeadAttention(D, num_heads, attn_drop)
        self.proj_drop = nn.Dropout(proj_drop)
        self.ln_1 = nn.LayerNorm(D)

    def forward(self, X):
        X = X + self.proj_drop(self.attn(self.ln_1(X)))
        return X

# --- Example Usage ---
if __name__ == '__main__':
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    D = 1024
    num_heads = 8
    seq_len = 512
    batch_size = 16
    attn_drop_rate = 0.1
    proj_drop_rate = 0.1

    X = torch.rand(batch_size, seq_len, D).to(device)
    model = AttentionBlock(D, num_heads, attn_drop_rate, proj_drop_rate).to(device)
    output = model(X)

    print("Input shape:", X.shape)
    print("Output shape:", output.shape)
