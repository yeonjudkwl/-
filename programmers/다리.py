def solution(bridge_length, weight, truck_weights):
    current_time = 0
    in_bridge = []
    
    while True:
        # 시간 경과
        current_time += 1

        # 다리 위에 트럭이 있으면
        if in_bridge:
            # 현재 경과 시간과 트럭이 다리를 건너는데 걸리는 시간(다리에 들어온 시간 + 다리를 건너는 시간)이 같으면
            if current_time == in_bridge[0][1]:
                # 빠져나간 트럭의 무게만큼 weight에 돌려줌
                weight = weight + in_bridge[0][0]
                # 다리에서 빠져나감
                in_bridge.pop(0)

        # 대기중인 트럭이 있으면
        if truck_weights:
            # 대기 첫 번째 트럭의 무게가 weight보다 작거나 같으면
            if truck_weights[0] <= weight:
                # 트럭무게 만큼 빠진 weight
                weight = weight - truck_weights[0]
                # 다리에 진입
                in_bridge.append((truck_weights.pop(0), current_time + bridge_length))
    
        
        if not in_bridge and not truck_weights:
            break

    return current_time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))