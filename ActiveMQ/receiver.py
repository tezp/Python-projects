import stomp
import time


class SampleListener(object):
    def on_message(self, headers, msg):
        print(msg)


conn = stomp.Connection10()
conn.set_listener('SampleListener', SampleListener())
conn.start()
conn.connect(headers={'client-id': 'SampleClient'})
conn.subscribe(destination='/topic/SampleTopic', id=1, ack='auto',
               headers={'activemq.subscriptionName': 'SampleSubscription'})
time.sleep(1)  # 1 secs
conn.disconnect()
