import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2] / "03_pydanticai_structured_output"))

from model import nvidia_model

MODEL_SMALL = nvidia_model("nvidia/nemotron-3.5-bolt-e4b")
MODEL_MEDIUM = nvidia_model("nvidia/nemotron-3.5-lightning-30b-a3b")
MODEL_LARGE = nvidia_model("nvidia/nemotron-3.5-super-vl-120b-a12b")
