# 실습 1

import numpy as np

# 입력 벡터: 값을 바꾸어 다른 예제도 계산할 수 있습니다.
u = np.array([4, 1, 1])
v = np.array([2, 1, 0])

u1, u2, u3 = u
v1, v2, v3 = v

# 행렬식 전개 부호: +, -, +
c1 = u2 * v3 - u3 * v2
c2 = -(u1 * v3 - u3 * v1)  # 가운데 항의 부호 주의
c3 = u1 * v2 - u2 * v1

result = np.array([c1, c2, c3])

print("i 성분:", c1)
print("j 성분:", c2)
print("k 성분:", c3)
print("u × v:", result)

# NumPy로 검산
reference = np.cross(u, v)
print("NumPy 결과:", reference)
print("결과 일치:", np.allclose(result, reference))

# 두 입력 벡터와 수직인지 확인
print("u · (u × v):", np.dot(u, result))
print("v · (u × v):", np.dot(v, result))


# 실습 2


import numpy as np

# 입력 벡터
u = np.array([3, -1, 2])
v = np.array([1, -2, 4])

u1, u2, u3 = u
v1, v2, v3 = v

# 성분별 계산: 전개 부호는 +, -, +
c1 = u2 * v3 - u3 * v2
c2 = -(u1 * v3 - u3 * v1)  # 가운데 항의 부호 주의
c3 = u1 * v2 - u2 * v1

result = np.array([c1, c2, c3])

print("i 성분:", c1)
print("j 성분:", c2)
print("k 성분:", c3)
print("u × v:", result)

# NumPy로 검산
print("NumPy 결과:", np.cross(u, v))

# 두 입력 벡터와 수직인지 확인
print("u · (u × v):", np.dot(u, result))
print("v · (u × v):", np.dot(v, result))


# 실습 3

import numpy as np

# 두 벡터
u = np.array([3, 1, 0])
v = np.array([1, 3, 2])

# 외적 계산
cross_product = np.cross(u, v)

# 넓이 = 외적 벡터의 길이
squared_length = np.dot(cross_product, cross_product)
area = np.linalg.norm(cross_product)

print("u × v =", cross_product)
print(f"넓이의 제곱 = {squared_length}")
print(f"평행사변형의 넓이 = {area:.6f}")

# 실습 4

import numpy as np

# 삼각형의 세 꼭짓점
A = np.array([-1, 2, 0])
B = np.array([2, 1, 3])
C = np.array([1, 1, -1])

# 같은 점 A에서 출발하는 두 변의 벡터
u = B - A
v = C - A

# 외적 계산
cross_product = np.cross(u, v)

# 외적의 길이는 평행사변형의 넓이
parallelogram_area = np.linalg.norm(cross_product)

# 삼각형의 넓이는 그 절반
triangle_area = parallelogram_area / 2

print("u =", u)
print("v =", v)
print("u × v =", cross_product)
print(f"평행사변형의 넓이 = {parallelogram_area:.6f}")
print(f"삼각형의 넓이 = {triangle_area:.6f}")

# 실습 5

import numpy as np

# 평행육면체를 이루는 세 벡터
u = np.array([4, 1, 1])
v = np.array([2, 1, 0])
w = np.array([0, 2, 3])

# 1. 외적과 밑면 넓이
cross_product = np.cross(u, v)
S = np.linalg.norm(cross_product)

# 2. 단위 법선벡터와 수직 높이
unit_normal = cross_product / S
h = abs(np.dot(w, unit_normal))

# 3. 밑면 넓이 × 수직 높이
V1 = S * h

# 4. 스칼라 삼중곱의 절댓값
V2 = abs(np.dot(cross_product, w))

# 5. 행렬식의 절댓값으로 검산
A = np.vstack([u, v, w])
V3 = abs(np.linalg.det(A))

print("u × v =", cross_product)
print(f"밑면 넓이 S = {S:.6f}")
print(f"수직 높이 h = {h:.6f}")
print(f"밑면 × 높이로 구한 체적 = {V1:.6f}")
print(f"삼중곱으로 구한 체적 = {V2:.6f}")
print(f"행렬식으로 구한 체적 = {V3:.6f}")

# 실습 6

import numpy as np

# 두 벡터
u = np.array([2, -4])
v = np.array([4, 2])

# 내적 계산
dot_uv = np.dot(u, v)
print("u · v =", dot_uv)

# 직교 여부 판단
if np.isclose(dot_uv, 0):
    print("두 벡터는 서로 직교합니다.")
else:
    print("두 벡터는 서로 직교하지 않습니다.")

# 사이각 계산
norm_product = np.linalg.norm(u) * np.linalg.norm(v)

if norm_product > 0:
    cos_theta = dot_uv / norm_product
    theta = np.degrees(
        np.arccos(np.clip(cos_theta, -1, 1))
    )
    print(f"두 벡터의 사이각 = {theta:.2f}도")
else:
    print("0벡터가 포함되면 사이각은 정의되지 않습니다.")