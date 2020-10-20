import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as tud
from torch.nn.parameter import Parameter
# vocab_size=30000
# embed_size=100
# out_embed = nn.Embedding(vocab_size, embed_size, sparse=False)
# an Embedding module containing 10 tensors of size 3
embedding = nn.Embedding(10, 3)
# a batch of 2 samples of 4 indices each
input = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])
h=embedding(input)
# print(h)
word_to_ix = {'hello':0,'world':999}
embedds =nn.Embedding(1000,5)
print(embedds.weight.data)

hello_ix =torch.LongTensor([word_to_ix['hello']])
# hello_ix=torch.autograd.Variable(hello_ix)
world_ix =torch.LongTensor([word_to_ix['world']])
hello_emded =embedds(hello_ix)
world_emded =embedds(world_ix)
print(hello_emded)
print(world_emded)