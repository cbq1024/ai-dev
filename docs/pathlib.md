# pathlib

> [!NOTE] Pathlib - 处理文件路径的现代方法
> 我们将学习如何使用 Pathlib 模块，并了解为什么它现在优于 os.path。在本视频中，我们将学习如何使用 Path
> 对象，它使用面向对象的方法对文件路径进行处理，而不是像以前使用 os.path 方法时那样使用字符串。许多代码库正在改用 Pathlib 和
> Path 对象，因此这是一项需要掌握的重要技能。

## 读取 .env 并获取

```pycon
import os
from pathlib2 import Path
from dotenv import load_dotenv

base_dir = Path(__file__).resolve()
root_path = base_dir.parents[2]
env_path = root_path / ".env"
load_dotenv(dotenv_path=env_path)

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

print(ACCESS_TOKEN)

```

