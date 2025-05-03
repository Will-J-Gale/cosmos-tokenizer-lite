## Cosmos Tokenizer Lite

* Lightweight version of https://github.com/NVIDIA/Cosmos-Tokenizer
* Only contains model/layer definitions
* Only kept requirements that the models/layers needed

## Install

### Locally
```bash
pip3 install -e .
```

### From git
```
pip3 install git+https://github.com/Will-J-Gale/cosmos-tokenizer-lite.git
```

## Using models
```python
import torch
from cosmos_tokenizer.networks import TokenizerConfigs
from cosmos_tokenizer.modules import Encoder, Decoder

encoder = Encoder(**TokenizerConfigs.CI.value)
decoder = Decoder(**TokenizerConfigs.CI.value)

input_tensor = torch.randn(8, 3, 256, 512)
latent = encoder(input_tensor)
model_output = decoder(latent)
```