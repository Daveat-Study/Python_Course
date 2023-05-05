# Python_Course

# Api Source
1. https://www.youtube.com/watch?v=0sOvCWFmrtA
2. https://fastapi.tiangolo.com/

# Python programming language
https://www.youtube.com/watch?v=8DvywoWv6fI&t=7s


-------------------- Activate Pip Script in Local Environment --------------------
=> source venv/bin/activate

-------------------- Host Local Api --------------------
=> uvicorn main:app 

# Source
https://www.youtube.com/watch?v=0sOvCWFmrtA&t=2364s


-------------------- Error --------------------
ERROR:    [Errno 48] Address already in use [Resource](https://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use)
Solution:
1. Search Processing ID of python
    => ps -fA | grep python
    COMMAND   PID   USER   FD   TYPE            DEVICE SIZE/OFF NODE NAME
    Python  61852 daveat    3u  IPv4 0x6d7fde6141b535b      0t0  TCP localhost:irdmi (LISTEN)
2. Kill python process:
    => kill -8 61852