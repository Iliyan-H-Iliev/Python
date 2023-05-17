from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())

bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())

p