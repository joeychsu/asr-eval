# asr-eval
ASR evaluation tool

## 目錄總覽
```
./
├── projects
│   └── caption
│       ├── data
│       │   ├── vUOxuMsss5o_label.srt
│       │   ├── vUOxuMsss5o_label.text
│       │   ├── vUOxuMsss5o_taption.srt
│       │   ├── vUOxuMsss5o_taption.text
│       │   ├── vUOxuMsss5o_whisper.srt
│       │   └── vUOxuMsss5o_whisper.text
│       ├── run.sh
│       └── src -> ../../src
├── README.md
└── src
    ├── compute-wer.py
    └── srt2single_text.py
```

## Projects

### caption
 - 進入目錄 projects/caption 並執行 run.sh
```
./run.sh
```
 - 就會得到以下結果: 
```
Loading [ data/vUOxuMsss5o_label.srt ] ...
Writing [ data/vUOxuMsss5o_label.text ] ...
Loading [ data/vUOxuMsss5o_whisper.srt ] ...
Writing [ data/vUOxuMsss5o_whisper.text ] ...
Loading [ data/vUOxuMsss5o_taption.srt ] ...
Writing [ data/vUOxuMsss5o_taption.text ] ...
Whisper CER(%)
Overall -> 6.99 % N=3474 C=3303 S=109 D=62 I=72

taption CER(%)
Overall -> 18.16 % N=3474 C=3092 S=251 D=131 I=249

Done!
```