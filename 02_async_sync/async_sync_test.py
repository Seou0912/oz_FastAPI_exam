from fastapi import APIRouter
import time
import asyncio
from concurrent.futures import ProcessPoolExecutor

router = APIRouter()


@router.get("/slow-async-ping")
def slow_async_ping():
    time.sleep(10)

    return {"message": "pong"}


@router.get("/fast-async-ping")
async def fast_async_ping():
    await asyncio.sleep(10)

    return {"message": "pong"}


@router.get("/cpu-bound-async")
async def cpu_bound_async():
    result = await cpu_intensive_task()
    return {"message": result}


def cpu_intensive_task():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    result = fibonacci(30)
    return result


# 비동기 라우트 내에서 멀티프로세싱을 사용하는 함수
@router.get("/cpu-bound-task")
async def cpu_bound_task():
    with ProcessPoolExecutor() as executor:
        # 비동기적으로 프로세스 실행 및 결과 대기
        result = await asyncio.get_event_loop().run_in_executor(
            executor, cpu_intensive_task
        )

    return {"result": result}
