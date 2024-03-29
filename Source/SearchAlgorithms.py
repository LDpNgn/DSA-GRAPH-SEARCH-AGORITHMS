from Space import *
from Constants import *

def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()
    
    #TODO: Implement DFS algorithm using open_set, closed_set, and father
    while open_set:
        v = open_set.pop()
        if g.is_goal(g.grid_cells[v]):
            print(len(closed_set))
            g.start.set_color(orange)
            g.goal.set_color(purple)
            g.draw(sc)
            
            while g.start.value != father[v]:
                i = father[v]
                a = g.grid_cells[i] 
                if i != g.start.value:
                    a.set_color(grey)
                    g.draw(sc)
                    pygame.draw.line(sc,green,(g.grid_cells[v].x, g.grid_cells[v].y),(a.x, a.y),2)
                    pygame.display.update()
                v =i
            pygame.draw.line(sc,green,(g.grid_cells[v].x, g.grid_cells[v].y),(g.start.x, g.start.y),2)
            pygame.display.update()
            return
    

        closed_set.append(v)
        g.grid_cells[v].set_color(yellow)
        g.draw(sc)
        neighbors:list[Node]
        neighbors=g.get_neighbors(g.grid_cells[v])
        
        for i in neighbors:
            if i.value not in closed_set:
                g.grid_cells[i.value].set_color(red)
                #g.draw(sc)
                if i.value not in open_set:
                    open_set.append(i.value)
                    father[i.value] = v
        g.grid_cells[v].set_color(blue)
        g.draw(sc)

    print(len(closed_set))  
    

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    #raise NotImplementedError('Not implemented')
    
    while open_set:
        v = open_set[0]
        del open_set[0]
        if g.is_goal(g.grid_cells[v]):
            g.grid_cells[father[v]].set_color(blue)
            g.start.set_color(orange)
            g.goal.set_color(purple)
            g.draw(sc)
            
            while g.start.value != father[v]:
                print(len(closed_set))
                i = father[v]
                a = g.grid_cells[i] 
                if i != g.start.value:
                    a.set_color(grey)
                    g.draw(sc)
                    pygame.draw.line(sc,green,(g.grid_cells[v].x, g.grid_cells[v].y),(a.x, a.y),2)
                    pygame.display.update()
                v =i
            pygame.draw.line(sc,green,(g.grid_cells[v].x, g.grid_cells[v].y),(g.start.x, g.start.y),2)
            pygame.display.update()
            return
    
        closed_set.append(v)
        g.grid_cells[v].set_color(yellow)
        g.draw(sc)
        neighbors:list[Node]
        neighbors=g.get_neighbors(g.grid_cells[v])
        
        for i in neighbors:
            if i.value not in closed_set:
                g.grid_cells[i.value].set_color(red)
                #g.draw(sc)
                if i.value not in open_set:
                    open_set.append(i.value)
                    father[i.value] = v
        g.grid_cells[v].set_color(blue)
        g.draw(sc) 
    

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    
    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    while open_set:
        a = min(open_set.values())
        v:int
        for i in open_set.keys():
            if open_set[i] == a:
                v = i
                del open_set[i]
                break
        if g.is_goal(g.grid_cells[v]):
            print(len(closed_set))
            g.grid_cells[father[v]].set_color(blue)
            g.start.set_color(orange)
            g.goal.set_color(purple)
            g.draw(sc)
            
            while g.start.value != father[v]:
                i = father[v]
                a = g.grid_cells[i] 
                if i != g.start.value:
                    a.set_color(grey)
                    g.draw(sc)
                    pygame.draw.line(sc,green,(g.grid_cells[v].x, g.grid_cells[v].y),(a.x, a.y),2)
                    pygame.display.update()
                v =i
            pygame.draw.line(sc,green,(g.grid_cells[v].x, g.grid_cells[v].y),(g.start.x, g.start.y),2)
            pygame.display.update()
            return


        closed_set.append(v)
        cost[v] = a
        g.grid_cells[v].set_color(yellow)
        g.draw(sc)
        neighbors:list[Node]
        neighbors=g.get_neighbors(g.grid_cells[v])
        
        for i in neighbors:
            if i.value not in closed_set:
                g.grid_cells[i.value].set_color(red)
                #g.draw(sc)
                cost_temp = cost[v] + g.g_cost(g.grid_cells[v], i)
                if cost_temp < cost[i.value]:
                    open_set[i.value] = cost_temp
                    father[i.value] = v
                    cost[i.value] = cost_temp
        g.grid_cells[v].set_color(blue)
        g.draw(sc)



def find_min_f_cost(g: Graph, open_set:list[Node], cost):
    min = g.get_len()
    temp = open_set[0]
    for i in open_set:
        if min > cost[i.value]:
            min = cost[i.value]
            temp = i
    return temp

def find_min_h_cost(g: Graph, open_set: list[Node], cost):
    min = 100000
    temp = open_set[0]
    for i in open_set:
        if min > cost[i.value] + g.heuristic(i):
            min = cost[i.value] + g.heuristic(i)
            temp = i
    return temp


def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm') 
    open_set:list[Node] = [g.start]
    closed_set = []
    father = [-1]*g.get_len()
    f_cost = [100_000]*g.get_len()
    f_cost[g.start.value]= 0
    
    if len(open_set) == 0:
        return
    for i in range(0, len(open_set)):
        while open_set:
            N_current: Node= find_min_h_cost(g, open_set, f_cost)
            if N_current.value != g.start.value:
                N_current.set_color(yellow)
                g.draw(sc)
                # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(N_current):
                print(len(closed_set))
                g.goal.set_color(purple)
                g.draw(sc)
                child = g.goal.value
                while child != g.start.value:
                    
                    pygame.draw.line(sc, green, (g.grid_cells[child].x, g.grid_cells[child].y), (g.grid_cells[father[child]].x, g.grid_cells[father[child]].y), 2)
                    pygame.display.flip()
                    child = father[child]
                    g.grid_cells[child].set_color(grey)
                    g.draw(sc)
                g.start.set_color(orange)
                g.draw(sc)
                return
            # xóa nút đã kiểm tra
            open_set.remove(N_current)
            # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(N_current)
            # Thay đổi màu cho nút đã được kiểm tra
            N_current.set_color(blue)
            g.draw(sc)
            # kiểm tra các biên và update cost
            neighbors: list[Node] = g.get_neighbors(N_current)
            while len(neighbors) != 0:
                if neighbors[0] not in closed_set:
                    if neighbors[0] not in open_set:
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            #g.draw(sc)
                        f_cost[neighbors[0].value] = f_cost[N_current.value] + g.g_cost(N_current, neighbors[0])
                        open_set.append(neighbors[0])
                        father[neighbors[0].value] = N_current.value
                neighbors.remove(neighbors[0])

    print(len(closed_set))
    raise NotImplementedError('Not implemented')