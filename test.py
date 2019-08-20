from admission_control_pb2_grpc import AdmissionControlStub
import grpc
from get_with_proof_pb2 import UpdateToLatestLedgerRequest
from get_with_proof_pb2 import GetAccountStateRequest, RequestItem
import struct

channel = grpc.insecure_channel("ac.testnet.libra.org:8000")
stub = AdmissionControlStub(channel)

last_version_seen = 0
req = UpdateToLatestLedgerRequest(client_known_version=last_version_seen, requested_items=[])

response = stub.UpdateToLatestLedger(req)
ledger_info = response.ledger_info_with_sigs.ledger_info

last_version_seen = ledger_info.version

print(last_version_seen)

toni = "4fe49d79e98ece0633b96363bc695dfc9fbbd32fffb9adae776f05f9b6104397"
acct = toni

account = GetAccountStateRequest(address=bytes.fromhex(acct))
item = RequestItem(get_account_state_request=account)
request = UpdateToLatestLedgerRequest(client_known_version=0, requested_items=[item])
response = stub.UpdateToLatestLedger(request)

state = response.response_items[0].get_account_state_response

acct_state = struct.unpack_from('=32sQ?QQQ', state.account_state_with_proof.blob.blob,
                           len(state.account_state_with_proof.blob.blob) - struct.calcsize('=32sQ?QQQ'))

account = bytes.hex(acct_state[0])
balance = acct_state[1] / 1000000
delegated = acct_state[2]
recv_events = acct_state[3]
sent_events = acct_state[4]
sq_num = acct_state[5]

print(balance)