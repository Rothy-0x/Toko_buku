from pypresence import Presence
import time

rpc = Presence("919567847259275284")
rpc.connect()
rpc.update(
    state="The Last of Us™ Part II",
    large_image="tlou",
    large_text="The Last of Us™ Part II",
    small_image="ps5",
    small_text="Rothy",
    start=time.time()
)
print("RPC sudah nyala")
input("\nTekan Enter untuk matikan aplikasi...")
rpc.close()
exit()
