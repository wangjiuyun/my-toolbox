from fastapi import FastAPI
from app.routers.toolbox import EchoRequest,EchoResponse,WordCountRequest,WordCountResponse

app = FastAPI(title="My Toolbox")

@app.get("/")
def root():
    return {"message":"hello toolbox"}

@app.get("/health")
def health():
    return {"status":"ok"}

    
@app.post("/echo", response_model=EchoResponse)
def echo(payload: EchoRequest):
      # TODO 3: 从 payload.text 取原始文本
    text = payload.text
      # TODO 4: 计算 normalized = 去首尾空格 + 转小写
    normalized = text.strip(" ").lower()
      # TODO 5: 计算 length = 原始文本长度(包含空格)
    length = len(text)
      # TODO 6: 返回 EchoResponse 实例
    return EchoResponse(
        original=text,
        normalized=normalized,
        length=length
    )



# todo 加一个word_count：int
@app.post("/word_count",response_model=WordCountResponse)
def word_count(payload: WordCountRequest) -> WordCountResponse:
    words = payload.text.split()
    return WordCountResponse(
        count = len(words),
        words= words
    )

