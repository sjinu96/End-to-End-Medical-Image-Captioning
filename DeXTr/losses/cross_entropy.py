import torch
import torch.nn as nn

class CrossEntropy(nn.Module):
    def __init__(self):
        super(CrossEntropy, self).__init__()
        self.criterion = nn.CrossEntropyLoss(ignore_index=-1)

    def forward(self, logit, target_seq):
        logit = logit.view(-1, logit.shape[-1]) # [11505,1809] / [13065,1809]
        
        #print("logit.shape:", logit.shape)
        #print("logit:", logit)
        target_seq = target_seq.view(-1) # [11505] / [13065]
        #print("target_seq.shape:", target_seq.shape)
        #print("target_seq:", target_seq)
        loss = self.criterion(logit, target_seq)
        return loss, {'CrossEntropy Loss': loss.item()}
