from pypresence import Presence
import time
# 919175832122065007
rpc = Presence("919565882919882752")
rpc.connect()


def stat1(rpc):
    rpc.update(
        state="Hey",
        small_image="abstac"
    )


def stat2(rpc):
    rpc.update(
        state="Fuck",
        small_image="abstac"
    )


def stat3(rpc):
    rpc.update(
        state="You",
        small_image="abstac"
    )


def stat4(rpc):
    rpc.update(
        state="Just Kidding",
        small_image="abstac"
    )


def stat5(rpc):
    rpc.update(
        state=":)",
        small_image="abstac"
    )


def stat6(rpc):
    rpc.update(
        state="I Love You <33",
        small_image="abstac"
    )


def da_rpc():
  while (True):
    stat1(rpc)
    time.sleep(0.7)
    stat2(rpc)
    time.sleep(0.7)
    stat3(rpc)
    time.sleep(0.7)
    stat4(rpc)
    time.sleep(0.7)
    stat5(rpc)
    time.sleep(0.7)
    stat6(rpc)
    time.sleep(2)


while (True):
    print("Presence Nyala")
    print("CTRL + C untuk matikan")
    da_rpc()
