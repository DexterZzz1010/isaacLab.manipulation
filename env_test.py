import torch

def test_torch_cuda():
    print("PyTorch 测试脚本")
    print("-" * 30)

    # 检测 PyTorch 是否安装
    print(f"PyTorch 是否可用: {'是' if torch.__version__ else '否'}")
    print(f"PyTorch 版本: {torch.__version__}")

    # 检测 CUDA 是否可用
    cuda_available = torch.cuda.is_available()
    print(f"CUDA 是否可用: {'是' if cuda_available else '否'}")

    if cuda_available:
        # 获取 CUDA 版本
        print(f"CUDA 版本: {torch.version.cuda}")
        # 获取 GPU 数量
        gpu_count = torch.cuda.device_count()
        print(f"可用 GPU 数量: {gpu_count}")
        for i in range(gpu_count):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")

        # 测试张量运算是否能在 GPU 上运行
        try:
            x = torch.tensor([1.0, 2.0, 3.0], device='cuda')
            print("CUDA 张量运算测试: 成功")
        except Exception as e:
            print(f"CUDA 张量运算测试: 失败 - {e}")
    else:
        print("未检测到可用的 CUDA 设备，跳过相关测试。")

    print("-" * 30)

if __name__ == "__main__":
    test_torch_cuda()
