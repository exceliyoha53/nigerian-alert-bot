2026-03-24 16:42:00,785 [INFO] __main__ - Building bot application...
2026-03-24 16:42:04,898 [INFO] __main__ - All handlers registered. Bot is running...
2026-03-24 16:42:04,909 [INFO] __main__ - Press Ctrl+C to stop 

2026-03-24 16:42:11,179 [INFO] httpx - HTTP Request: POST https://api.telegram.org/ "HTTP/1.1 200 OK"
2026-03-24 16:42:11,372 [INFO] httpx - HTTP Request: POST https://api.telegram.org/ "HTTP/1.1 200 OK"
2026-03-24 16:42:11,383 [INFO] telegram.ext.Application - Application started
2026-03-24 16:42:31,225 [INFO] httpx - HTTP Request: POST https://api.telegram.org/ "HTTP/1.1 200 OK"
2026-03-24 16:45:09,010 [INFO] bot.handlers - User 1841231351 trigger /start
2026-03-24 16:45:14,644 [ERROR] telegram.ext.Application - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 101, in map_httpcore_exceptions
    yield
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 394, in handle_async_request
    resp = await self._pool.handle_async_request(req)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 256, in handle_async_request
    raise exc from None
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 236, in handle_async_request
    response = await connection.handle_async_request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 103, in handle_async_request
    return await self._connection.handle_async_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\http11.py", line 136, in handle_async_request
    raise exc
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\http11.py", line 106, in handle_async_request
    ) = await self._receive_response_headers(**kwargs)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\http11.py", line 177, in _receive_response_headers
    event = await self._receive_event(timeout=timeout)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\http11.py", line 217, in _receive_event
    data = await self._network_stream.read(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_backends\anyio.py", line 32, in read
    with map_exceptions(exc_map):
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ReadTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 279, in do_request
    res = await self._client.request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1540, in request
    return await self.send(request, auth=auth, follow_redirects=follow_redirects)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1629, in send
    response = await self._send_handling_auth(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1657, in _send_handling_auth
    response = await self._send_handling_redirects(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1694, in _send_handling_redirects
    response = await self._send_single_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1730, in _send_single_request
    response = await transport.handle_async_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 393, in handle_async_request
    with map_httpcore_exceptions():
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ReadTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_application.py", line 1315, in process_update
    await coroutine
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_handlers\basehandler.py", line 159, in handle_update
    return await self.callback(update, context)
  File "C:\Users\hp\nigerian-alert-bot\bot\handlers.py", line 52, in start_handler
    await update.message.reply_text(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_message.py", line 2106, in reply_text
    return await self.get_bot().send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 3118, in send_message
    return await super().send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 1123, in send_message
    return await self._send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 630, in _send_message
    result = await super()._send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 820, in _send_message
    result = await self._post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 704, in _post
    return await self._do_post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 370, in _do_post
    return await super()._do_post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 733, in _do_post
    result = await request.post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 198, in post
    result = await self._request_wrapper(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 305, in _request_wrapper
    code, payload = await self.do_request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 296, in do_request
    raise TimedOut from err
telegram.error.TimedOut: Timed out
2026-03-24 16:45:19,233 [INFO] httpx - HTTP Request: POST https://api.telegram.org/ "HTTP/1.1 200 OK"
2026-03-24 16:45:29,439 [INFO] httpx - HTTP Request: POST https://api.telegram.org/
2026-03-24 16:45:36,096 [INFO] bot.handlers - User 1841231351 triggered /latest
2026-03-24 16:45:42,310 [ERROR] telegram.ext.Application - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 101, in map_httpcore_exceptions
    yield
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 394, in handle_async_request
    resp = await self._pool.handle_async_request(req)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 256, in handle_async_request
    raise exc from None
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 236, in handle_async_request
    response = await connection.handle_async_request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 101, in handle_async_request
    raise exc
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 78, in handle_async_request
    stream = await self._connect(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 156, in _connect
    stream = await stream.start_tls(**kwargs)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_backends\anyio.py", line 67, in start_tls
    with map_exceptions(exc_map):
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 279, in do_request
    res = await self._client.request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1540, in request
    return await self.send(request, auth=auth, follow_redirects=follow_redirects)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1629, in send
    response = await self._send_handling_auth(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1657, in _send_handling_auth
    response = await self._send_handling_redirects(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1694, in _send_handling_redirects
    response = await self._send_single_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1730, in _send_single_request
    response = await transport.handle_async_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 393, in handle_async_request
    with map_httpcore_exceptions():
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_application.py", line 1315, in process_update
    await coroutine
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_handlers\basehandler.py", line 159, in handle_update
    return await self.callback(update, context)
  File "C:\Users\hp\nigerian-alert-bot\bot\handlers.py", line 63, in latest_handler
    await update.message.reply_text("Fetching latest jobs...")
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_message.py", line 2106, in reply_text
    return await self.get_bot().send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 3118, in send_message
    return await super().send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 1123, in send_message
    return await self._send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 630, in _send_message
    result = await super()._send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 820, in _send_message
    result = await self._post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 704, in _post
    return await self._do_post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 370, in _do_post
    return await super()._do_post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 733, in _do_post
    result = await request.post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 198, in post
    result = await self._request_wrapper(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 305, in _request_wrapper
    code, payload = await self.do_request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 296, in do_request
    raise TimedOut from err
telegram.error.TimedOut: Timed out
2026-03-24 16:45:46,310 [INFO] httpx - HTTP Request: POST https://api.telegram.org/ "HTTP/1.1 200 OK"
2026-03-24 16:45:56,911 [INFO] httpx - HTTP Request: POST https://api.telegram.org/ "HTTP/1.1 200 OK"
2026-03-24 16:46:08,353 [INFO] httpx - HTTP Request: POST https://api.telegram.org/ "HTTP/1.1 200 OK"
2026-03-24 16:46:09,663 [INFO] httpx - HTTP Request: POST https://api.telegram.org/ "HTTP/1.1 200 OK"
2026-03-24 16:46:09,668 [INFO] bot.handlers - User 1841231351 triggered /latest
2026-03-24 16:46:14,858 [ERROR] telegram.ext.Application - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 101, in map_httpcore_exceptions
    yield
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 394, in handle_async_request
    resp = await self._pool.handle_async_request(req)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 256, in handle_async_request
    raise exc from None
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 236, in handle_async_request
    response = await connection.handle_async_request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 101, in handle_async_request
    raise exc
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 78, in handle_async_request
    stream = await self._connect(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 156, in _connect
    stream = await stream.start_tls(**kwargs)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_backends\anyio.py", line 67, in start_tls
    with map_exceptions(exc_map):
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 279, in do_request
    res = await self._client.request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1540, in request
    return await self.send(request, auth=auth, follow_redirects=follow_redirects)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1629, in send
    response = await self._send_handling_auth(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1657, in _send_handling_auth
    response = await self._send_handling_redirects(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1694, in _send_handling_redirects
    response = await self._send_single_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1730, in _send_single_request
    response = await transport.handle_async_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 393, in handle_async_request
    with map_httpcore_exceptions():
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_application.py", line 1315, in process_update
    await coroutine
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_handlers\basehandler.py", line 159, in handle_update
    return await self.callback(update, context)
  File "C:\Users\hp\nigerian-alert-bot\bot\handlers.py", line 63, in latest_handler
    await update.message.reply_text("Fetching latest jobs...")
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_message.py", line 2106, in reply_text
    return await self.get_bot().send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 3118, in send_message
    return await super().send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 1123, in send_message
    return await self._send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 630, in _send_message
    result = await super()._send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 820, in _send_message
    result = await self._post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 704, in _post
    return await self._do_post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 370, in _do_post
    return await super()._do_post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 733, in _do_post
    result = await request.post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 198, in post
    result = await self._request_wrapper(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 305, in _request_wrapper
    code, payload = await self.do_request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 296, in do_request
    raise TimedOut from err
telegram.error.TimedOut: Timed out
2026-03-24 16:47:01,950 [INFO] httpx - HTTP Request: POST https://api.telegram.org/ "HTTP/1.1 200 OK"
2026-03-24 16:49:35,061 [INFO] bot.handlers - User 1841231351 triggererd /search with args: ['Abuja']
2026-03-24 16:49:37,270 [INFO] services.database - Search for 'Abuja' returned 9 results
2026-03-24 16:49:44,206 [ERROR] telegram.ext.Application - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 101, in map_httpcore_exceptions
    yield
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 394, in handle_async_request
    resp = await self._pool.handle_async_request(req)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 256, in handle_async_request
    raise exc from None
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 236, in handle_async_request
    response = await connection.handle_async_request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 103, in handle_async_request
    return await self._connection.handle_async_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\http11.py", line 136, in handle_async_request
    raise exc
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\http11.py", line 106, in handle_async_request
    ) = await self._receive_response_headers(**kwargs)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\http11.py", line 177, in _receive_response_headers
    event = await self._receive_event(timeout=timeout)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\http11.py", line 217, in _receive_event
    data = await self._network_stream.read(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_backends\anyio.py", line 32, in read
    with map_exceptions(exc_map):
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ReadTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 279, in do_request
    res = await self._client.request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1540, in request
    return await self.send(request, auth=auth, follow_redirects=follow_redirects)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1629, in send
    response = await self._send_handling_auth(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1657, in _send_handling_auth
    response = await self._send_handling_redirects(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1694, in _send_handling_redirects
    response = await self._send_single_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1730, in _send_single_request
    response = await transport.handle_async_request(request)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 393, in handle_async_request
    with map_httpcore_exceptions():
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ReadTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_application.py", line 1315, in process_update
    await coroutine
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_handlers\basehandler.py", line 159, in handle_update
    return await self.callback(update, context)
  File "C:\Users\hp\nigerian-alert-bot\bot\handlers.py", line 93, in search_handler
    await _do_location_search(update, location)
  File "C:\Users\hp\nigerian-alert-bot\bot\handlers.py", line 151, in _do_location_search
    await update.message.reply_text(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_message.py", line 2106, in reply_text
    return await self.get_bot().send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 3118, in send_message
    return await super().send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 1123, in send_message
    return await self._send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 630, in _send_message
    result = await super()._send_message(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 820, in _send_message
    result = await self._post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 704, in _post
    return await self._do_post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 370, in _do_post
    return await super()._do_post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 733, in _do_post
    result = await request.post(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 198, in post
    result = await self._request_wrapper(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 305, in _request_wrapper
    code, payload = await self.do_request(
  File "C:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 296, in do_request
    raise TimedOut from err
telegram.error.TimedOut: Timed out
2026-03-24 16:49:49,865 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 16:50:00,105 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 16:50:07,025 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 16:50:07,037 [INFO] bot.handlers - User 1841231351 trigerred /stats
2026-03-24 16:50:07,504 [INFO] services.database - Vault stats fetched � total: 48, last scrape: 2026-03-21 00:33:58.681915
2026-03-24 16:50:09,386 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/sendMessage "HTTP/1.1 200 OK"
bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:03:46,329 [INFO] telegram.ext.Application - Application is stopping. This might take a moment.
2026-03-24 17:03:46,332 [INFO] telegram.ext.Application - Application.stop() complete
2026-03-24 17:15:13,741 [INFO] __main__ - Building bot application...
2026-03-24 17:15:13,812 [INFO] __main__ - All handlers registered. Bot is running...
2026-03-24 17:15:13,814 [INFO] __main__ - Press Ctrl+C to stop 

2026-03-24 17:15:21,170 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getMe "HTTP/1.1 200 OK"
2026-03-24 17:15:21,415 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/deleteWebhook "HTTP/1.1 200 OK"
2026-03-24 17:15:21,442 [INFO] telegram.ext.Application - Application started
2026-03-24 17:15:32,227 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:15:42,886 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:15:53,547 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:16:12,166 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:16:12,181 [INFO] bot.handlers - User 1841231351 trigger /start
2026-03-24 17:16:23,181 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:16:33,914 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:16:42,415 [ERROR] telegram.ext.Application - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 101, in map_httpcore_exceptions
    yield
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 394, in handle_async_request
    resp = await self._pool.handle_async_request(req)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 256, in handle_async_request
    raise exc from None
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 236, in handle_async_request
    response = await connection.handle_async_request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 101, in handle_async_request
    raise exc
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 78, in handle_async_request
    stream = await self._connect(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 156, in _connect
    stream = await stream.start_tls(**kwargs)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_backends\anyio.py", line 67, in start_tls
    with map_exceptions(exc_map):
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 279, in do_request
    res = await self._client.request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1540, in request
    return await self.send(request, auth=auth, follow_redirects=follow_redirects)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1629, in send
    response = await self._send_handling_auth(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1657, in _send_handling_auth
    response = await self._send_handling_redirects(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1694, in _send_handling_redirects
    response = await self._send_single_request(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1730, in _send_single_request
    response = await transport.handle_async_request(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 393, in handle_async_request
    with map_httpcore_exceptions():
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_application.py", line 1315, in process_update
    await coroutine
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_handlers\basehandler.py", line 159, in handle_update
    return await self.callback(update, context)
  File "c:\Users\hp\nigerian-alert-bot\bot\handlers.py", line 52, in start_handler
    await update.message.reply_text(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_message.py", line 2106, in reply_text
    return await self.get_bot().send_message(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 3118, in send_message
    return await super().send_message(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 1123, in send_message
    return await self._send_message(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 630, in _send_message
    result = await super()._send_message(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 820, in _send_message
    result = await self._post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 704, in _post
    return await self._do_post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 370, in _do_post
    return await super()._do_post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 733, in _do_post
    result = await request.post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 198, in post
    result = await self._request_wrapper(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 305, in _request_wrapper
    code, payload = await self.do_request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 296, in do_request
    raise TimedOut from err
telegram.error.TimedOut: Timed out
2026-03-24 17:16:44,166 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:17:35,509 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:18:27,117 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:18:38,374 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:18:49,159 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:18:56,880 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:18:56,887 [INFO] bot.handlers - User 1841231351 triggered /latest
2026-03-24 17:19:07,680 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:19:17,959 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:19:29,127 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:19:30,098 [ERROR] telegram.ext.Application - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 101, in map_httpcore_exceptions
    yield
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 394, in handle_async_request
    resp = await self._pool.handle_async_request(req)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 256, in handle_async_request
    raise exc from None
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 236, in handle_async_request
    response = await connection.handle_async_request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 101, in handle_async_request
    raise exc
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 78, in handle_async_request
    stream = await self._connect(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 156, in _connect
    stream = await stream.start_tls(**kwargs)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_backends\anyio.py", line 67, in start_tls
    with map_exceptions(exc_map):
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 279, in do_request
    res = await self._client.request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1540, in request
    return await self.send(request, auth=auth, follow_redirects=follow_redirects)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1629, in send
    response = await self._send_handling_auth(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1657, in _send_handling_auth
    response = await self._send_handling_redirects(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1694, in _send_handling_redirects
    response = await self._send_single_request(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1730, in _send_single_request
    response = await transport.handle_async_request(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 393, in handle_async_request
    with map_httpcore_exceptions():
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_application.py", line 1315, in process_update
    await coroutine
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_handlers\basehandler.py", line 159, in handle_update
    return await self.callback(update, context)
  File "c:\Users\hp\nigerian-alert-bot\bot\handlers.py", line 63, in latest_handler
    await update.message.reply_text("Fetching latest jobs...")
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_message.py", line 2106, in reply_text
    return await self.get_bot().send_message(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 3118, in send_message
    return await super().send_message(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 1123, in send_message
    return await self._send_message(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 630, in _send_message
    result = await super()._send_message(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 820, in _send_message
    result = await self._post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 704, in _post
    return await self._do_post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 370, in _do_post
    return await super()._do_post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 733, in _do_post
    result = await request.post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 198, in post
    result = await self._request_wrapper(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 305, in _request_wrapper
    code, payload = await self.do_request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 296, in do_request
    raise TimedOut from err
telegram.error.TimedOut: Timed out
2026-03-24 17:19:39,320 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:19:49,804 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:20:00,484 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:20:10,759 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:20:20,964 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:20:31,584 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:20:42,237 [INFO] httpx - HTTP Request: POST https://api.telegram.org/bottoken/getUpdates "HTTP/1.1 200 OK"
2026-03-24 17:21:08,542 [ERROR] asyncio - Task exception was never retrieved
future: <Task finished name='Task-85' coro=<Updater._start_polling.<locals>.polling_action_cb() done, defined at c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_updater.py:338> exception=TimedOut('Timed out')>
Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 101, in map_httpcore_exceptions
    yield
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 394, in handle_async_request
    resp = await self._pool.handle_async_request(req)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 256, in handle_async_request
    raise exc from None
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 236, in handle_async_request
    response = await connection.handle_async_request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 101, in handle_async_request
    raise exc
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 78, in handle_async_request
    stream = await self._connect(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 156, in _connect
    stream = await stream.start_tls(**kwargs)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_backends\anyio.py", line 67, in start_tls
    with map_exceptions(exc_map):
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 279, in do_request
    res = await self._client.request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1540, in request
    return await self.send(request, auth=auth, follow_redirects=follow_redirects)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1629, in send
    response = await self._send_handling_auth(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1657, in _send_handling_auth
    response = await self._send_handling_redirects(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1694, in _send_handling_redirects
    response = await self._send_single_request(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1730, in _send_single_request
    response = await transport.handle_async_request(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 393, in handle_async_request
    with map_httpcore_exceptions():
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_updater.py", line 340, in polling_action_cb
    updates = await self.bot.get_updates(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 672, in get_updates
    updates = await super().get_updates(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 4865, in get_updates
    await self._post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 704, in _post
    return await self._do_post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 370, in _do_post
    return await super()._do_post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 733, in _do_post
    result = await request.post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 198, in post
    result = await self._request_wrapper(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 305, in _request_wrapper
    code, payload = await self.do_request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 296, in do_request
    raise TimedOut from err
telegram.error.TimedOut: Timed out
2026-03-24 17:21:15,501 [ERROR] telegram.ext.Updater - Error while calling `get_updates` one more time to mark all fetched updates. Suppressing error to ensure graceful shutdown. When polling for updates is restarted, updates may be fetched again. Please adjust timeouts via `ApplicationBuilder` or the parameter `get_updates_request` of `Bot`.
Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 101, in map_httpcore_exceptions
    yield
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 394, in handle_async_request
    resp = await self._pool.handle_async_request(req)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 256, in handle_async_request
    raise exc from None
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection_pool.py", line 236, in handle_async_request
    response = await connection.handle_async_request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 101, in handle_async_request
    raise exc
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 78, in handle_async_request
    stream = await self._connect(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_async\connection.py", line 156, in _connect
    stream = await stream.start_tls(**kwargs)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_backends\anyio.py", line 67, in start_tls
    with map_exceptions(exc_map):
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpcore\_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 279, in do_request
    res = await self._client.request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1540, in request
    return await self.send(request, auth=auth, follow_redirects=follow_redirects)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1629, in send
    response = await self._send_handling_auth(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1657, in _send_handling_auth
    response = await self._send_handling_redirects(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1694, in _send_handling_redirects
    response = await self._send_single_request(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_client.py", line 1730, in _send_single_request
    response = await transport.handle_async_request(request)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 393, in handle_async_request
    with map_httpcore_exceptions():
  File "C:\Program Files\Python310\lib\contextlib.py", line 153, in __exit__
    self.gen.throw(typ, value, traceback)
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\httpx\_transports\default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_updater.py", line 400, in _get_updates_cleanup
    await self.bot.get_updates(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 672, in get_updates
    updates = await super().get_updates(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 4865, in get_updates
    await self._post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 704, in _post
    return await self._do_post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\ext\_extbot.py", line 370, in _do_post
    return await super()._do_post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\_bot.py", line 733, in _do_post
    result = await request.post(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 198, in post
    result = await self._request_wrapper(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_baserequest.py", line 305, in _request_wrapper
    code, payload = await self.do_request(
  File "c:\Users\hp\nigerian-alert-bot\venv\lib\site-packages\telegram\request\_httpxrequest.py", line 296, in do_request
    raise TimedOut from err
telegram.error.TimedOut: Timed out
2026-03-24 17:21:15,590 [INFO] telegram.ext.Application - Application is stopping. This might take a moment.
2026-03-24 17:21:15,617 [INFO] telegram.ext.Application - Application.stop() complete
