import torch

print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Device:", torch.cuda.get_device_name(0))
    print("Capability:", torch.cuda.get_device_capability(0))
    x = torch.randn(1024, 1024, device="cuda")
    y = torch.mm(x, x)
    print("GPU matmul OK, shape:", y.shape)
else:
    print("NOTE: If False, install a CUDA-enabled PyTorch wheel (cu121).")
