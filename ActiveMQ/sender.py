import stomp

conn = stomp.Connection10()
conn.start()
conn.connect()
conn.send('/topic/SampleTopic', 'this is Sample message from Sender')
conn.disconnect()
