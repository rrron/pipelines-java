import pull_request

comment = """
## Useful Table

| Item | Col1  | Col2  | Col3  | Col4  |
|---|---|---|---|---|
| 1 | a | b | c | d |
| 2 | a | b | c | d |
| 3 | a | b | c | d |

Some additional text here
"""
msg = pull_request.Message()
result = msg.add(comment=comment)
if result is False:
    print("Sending message failed")