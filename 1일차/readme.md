## ollama pull 가능 모형(2026.6)

---

### Qwen (Alibaba)

| 모델명 | pull 명령 | 특징 |
|---|---|---|
| Qwen3 | `ollama run qwen3` | 최신 Dense/MoE 혼합 패밀리, thinking mode 지원 |
| Qwen3 (8B) | `ollama run qwen3:8b` | 8B 사이즈 |
| Qwen3 (30B-A3B) | `ollama run qwen3:30b-a3b` | MoE, QwQ-32B 능가 |
| Qwen3 (235B-A22B) | `ollama run qwen3:235b-a22b` | 플래그십, DeepSeek-R1급 |
| Qwen3.5 | `ollama run qwen3.5` | 멀티모달, 256K context, thinking mode |
| Qwen3.5 (4B) | `ollama run qwen3.5:4b` | 8GB RAM에서 동작 |
| Qwen3.6 (27B) | `ollama run qwen3.6:27b` | 소비자 GPU 최고 성능, SWE-bench 77.2% |
| Qwen2.5 | `ollama run qwen2.5` | 0.5B~72B, 수학/다국어 강점 |
| Qwen2.5-Coder (32B) | `ollama run qwen2.5-coder:32b` | HumanEval 92.7% |
| qwen3-coder (30B) | `ollama run qwen3-coder:30b` | 코딩 에이전트 특화 |

---

### Gemma (Google DeepMind)

| 모델명 | pull 명령 | 특징 |
|---|---|---|
| Gemma4 | `ollama run gemma4` | 멀티모달, tool calling, 128K context |
| Gemma4 (E4B) | `ollama run gemma4:e4b` | 8GB RAM에서 동작 |
| Gemma4 (12B) | `ollama run gemma4:12b` | 16GB RAM에서 동작, 최신 추가 |
| Gemma4 (26B) | `ollama run gemma4:26b` | 85 t/s 추론 속도 |
| Gemma4 (E27B) | `ollama run gemma4:e27b` | 최고 성능 버전 |
| Gemma2 | `ollama run gemma2` | 2B/9B/27B, 구세대 |
| Gemma3n | `ollama run gemma3n` | 모바일/엣지 디바이스 특화 |

---

### Llama (Meta)

| 모델명 | pull 명령 | 특징 |
|---|---|---|
| Llama3.2 (3B) | `ollama run llama3.2:3b` | 8개 언어, 다운로드 1위 |
| Llama3.2 (1B) | `ollama run llama3.2:1b` | 초경량 |
| Llama3.2-Vision (11B) | `ollama run llama3.2-vision:11b` | 이미지 이해 |
| Llama3.3 (70B) | `ollama run llama3.3:70b` | Llama 3.1 405B급 성능 |
| Llama4 Scout | `ollama run llama4:scout` | MoE, 10M context, 멀티모달 |
| Llama4 Maverick | `ollama run llama4:maverick` | 범용 대화 최고 성능 |

## 코딩/에이전트 → `qwen3.6:27b` 또는 `qwen2.5-coder:32b`, 멀티모달/tool calling → `gemma4:12b`, 범용/경량 → `llama3.2:3b`
