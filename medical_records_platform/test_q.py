from django_q.tasks import async_task
import sys
import queue

sys.path.insert(1, './medical_records_platform/myapi')
sys.path.insert(2, './medical_records_platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

def test_q():
    json_payload = {
        'Perform': 'a',
        'simple': 'queuing',
        'test': 'for',
        'EC': '530'
    }

    async_task(queue.q_stub_func, json_payload, 2)
    async_task(queue.q_stub_func, json_payload, 4)
    async_task(queue.q_stub_func, json_payload, 6)
    async_task(queue.q_stub_func, json_payload, 8)

    return print('Completed Queue')