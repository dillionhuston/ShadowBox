import logger, traceback, functools, asyncio
from typing import Any, Optional, Callable, TypeVar, cast

_FuncT = TypeVar("_FuncT", bound=Callable[..., Any])

def TryWithLogError(func: Callable[..., Any], *args, errorReturn: Any = None,
                    errorFunc: Optional[Callable[[Exception], None]] = None,
                    errorCustomLogFormat: Optional[Callable[[Exception], str]] = None,
                    functionName: Optional[str] = None, includeTraceback: bool = False,
                    **kwargs)-> Any:
    """Execute the given function in a try-except block, log any exception occurred."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        error_str = errorCustomLogFormat(e) if errorCustomLogFormat else \
            f"{type(e).__name__} occurred{'' if not functionName else f' ({functionName})'}: {str(e)}"
        if includeTraceback:
            error_str += f"\n--- Traceback ---\n{traceback.format_exc()}";
        
        if errorFunc:
            errorFunc(e)
        
        logger.Logger.LogError(error_str)
        return errorReturn
    
def LogError(func: Callable[..., Any], *args, 
             errorFunc: Optional[Callable[[Exception], None]] = None,
             errorCustomLogFormat: Optional[Callable[[Exception], str]] = None,
             functionName: Optional[str] = None,
             includeTraceback: bool = False, **kwargs) -> Any:
    """TryWithLogError, but throw error after log."""
    def handleError(e: Exception):
        errorFunc(e)
        raise e
    return TryWithLogError(
        func, *args,
        errorReturn=None, errorFunc=handleError,
        errorCustomLogFormat=errorCustomLogFormat,
        functionName=functionName,
        includeTraceback=includeTraceback
    )

def TryWithLogErrorDecorator(errorReturn: Any = None,
                             errorFunc: Optional[Callable[[Exception], None]] = None,
                             errorCustomLogFormat: Optional[Callable[[Exception], str]] = None,
                             functionName: Optional[str] = None,
                             includeTraceback: bool = False) -> Callable[[_FuncT], _FuncT]:
    """TryWithLogError as a decorator."""
    
    def decorator(func: _FuncT) -> _FuncT:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return TryWithLogError(
                func, *args, 
                errorReturn=errorReturn,
                errorFunc=errorFunc,
                errorCustomLogFormat=errorCustomLogFormat,
                functionName=functionName,
                includeTraceback=includeTraceback,
                **kwargs)
        return cast(_FuncT, wrapper)
    return decorator

def LogErrorDecorator(errorFunc: Optional[Callable[[Exception], None]] = None,
                      errorCustomLogFormat: Optional[Callable[[Exception], str]] = None,
                      functionName: Optional[str] = None,
                      includeTraceback: bool = False) -> Callable[[_FuncT], _FuncT]:
    """TryWithLogErrorDecorator, but only for log error."""
    def decorator(func: _FuncT) -> _FuncT:
        def handleError(e: Exception):
            errorFunc(e)
            raise e
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return TryWithLogError(
                func, *args,
                errorReturn=None, errorFunc=handleError,
                errorCustomLogFormat=errorCustomLogFormat,
                functionName=functionName,
                includeTraceback=includeTraceback
            )
        return cast(_FuncT, wrapper)
    return decorator

async def TryWithLogErrorAsync(func: Callable[..., Any], *args, errorReturn: Any = None,
                    errorFunc: Optional[Callable[[Exception], None]] = None,
                    errorCustomLogFormat: Optional[Callable[[Exception], str]] = None,
                    functionName: Optional[str] = None, includeTraceback: bool = False,
                    **kwargs)-> Any:
    """Execute the given async function in a try-except block, log any exception occurred."""
    try:
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
            return func(*args, **kwargs)
    except Exception as e:
        error_str = errorCustomLogFormat(e) if errorCustomLogFormat else \
            f"{type(e).__name__} occurred{'' if not functionName else f' ({functionName})'}: {str(e)}"
        if includeTraceback:
            error_str += f"\n--- Traceback ---\n{traceback.format_exc()}";
        
        if errorFunc:
            if asyncio.iscoroutinefunction(errorFunc):
                await errorFunc(e)
            else:
                errorFunc(e)
        
        logger.Logger.LogError(error_str)
        return errorReturn

def TryWithLogErrorAsyncDecorator(errorReturn: Any = None,
                                  errorFunc: Optional[Callable[[Exception], None]] = None,
                                  errorCustomLogFormat: Optional[Callable[[Exception], str]] = None,
                                  functionName: Optional[str] = None,
                                  includeTraceback: bool = False) -> Callable[[_FuncT], _FuncT]:
    """TryWithLogErrorAsync as a decorator."""
    
    def decorator(func: _FuncT) -> _FuncT:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            return await TryWithLogErrorAsync(
                func, *args, 
                errorReturn=errorReturn,
                errorFunc=errorFunc,
                errorCustomLogFormat=errorCustomLogFormat,
                functionName=functionName,
                includeTraceback=includeTraceback,
                **kwargs)
        return cast(_FuncT, wrapper)
    return decorator

async def LogErrorAsync(func: Callable[..., Any], *args, 
             errorFunc: Optional[Callable[[Exception], None]] = None,
             errorCustomLogFormat: Optional[Callable[[Exception], str]] = None,
             functionName: Optional[str] = None,
             includeTraceback: bool = False, **kwargs) -> Any:
    """TryWithLogErrorAsync, but throw error after log."""
    async def handleError(e: Exception):
        if errorFunc:
            if asyncio.iscoroutinefunction(errorFunc):
                await errorFunc(e)
            else:
                errorFunc(e)
        raise e
    return await TryWithLogErrorAsync(
        func, *args,
        errorReturn=None, errorFunc=handleError,
        errorCustomLogFormat=errorCustomLogFormat,
        functionName=functionName,
        includeTraceback=includeTraceback
    )

def LogErrorAsyncDecorator(errorFunc: Optional[Callable[[Exception], None]] = None,
                      errorCustomLogFormat: Optional[Callable[[Exception], str]] = None,
                      functionName: Optional[str] = None,
                      includeTraceback: bool = False) -> Callable[[_FuncT], _FuncT]:
    """TryWithLogErrorAsyncDecorator, but only for log error."""
    def decorator(func: _FuncT) -> _FuncT:
        async def handleError(e: Exception):
            if errorFunc:
                if asyncio.iscoroutinefunction(errorFunc):
                    await errorFunc(e)
                else:
                    errorFunc(e)
            raise e
        
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            return await TryWithLogErrorAsync(
                func, *args,
                errorReturn=None, errorFunc=handleError,
                errorCustomLogFormat=errorCustomLogFormat,
                functionName=functionName,
                includeTraceback=includeTraceback
            )
        return cast(_FuncT, wrapper)
    return decorator