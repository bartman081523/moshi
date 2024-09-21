class QuantizationConfig:
    def __init__(self, quantization_level=None, num_codebooks=None, codebook_size=None):
        self.quantization_level = quantization_level
        self.num_codebooks = num_codebooks
        self.codebook_size = codebook_size
