import sys

# Leitura de dados
def read_input_file(file_path: str):
    """
    Leitura do arquivo de entrada

    Formato esperado pelo arquivo:

    N                   --> Número de vértices
    N linhas com N ints --> Matriz de adjacência
    origin              --> Indice de origem do vértice
    destination         --> Indice do vertice do destino
    K                   --> Máximo de vertices no caminho
    """

    with open(file_path, 'r', encoding='utf-8') as f:
        # Lê todas as linhas, ignorando linhas vazias e comentários
        lines = [
            line.strip() for line in f 
            if line.strip() and not line.strip().startswith('#')
        ]
        
    if not lines:
        raise ValueError("O arquivo de entrada está vazio ou não contém dados válidos.")

    idx = 0 
    
    n = int(lines[idx])
    idx += 1
    
    matrix = []
    
    for _ in range(n):
        line_values = list(map(int, lines[idx].split()))
        if len(line_values) != n:
            raise ValueError(
                f"Linha da Matriz com o tamanho inesperado: esperado {n}, "
                f"Obtido {len(line_values)}"
            )
        
        matrix.append(line_values)
        idx += 1

    origin = int(lines[idx])
    idx += 1
    destination = int(lines[idx])
    idx += 1
    max_vertices = int(lines[idx])
    idx += 1

    return n, matrix, origin, destination, max_vertices


def find_max_weight_path(n, matrix, origin, destination, max_vertices):
    """
    Busca de todos os caminhos mais simples de 'origin' a 'destination' 
    com o máximo de K vértices, sempre retornando o de maior peso.
    """

    best_weight: int | None = None
    best_path: list | None = None
 
    def dfs(current: int, path: list, accumulated_weight: int, visited: set):
        nonlocal best_weight, best_path
 
        if current == destination:
            if best_weight is None or accumulated_weight > best_weight:
                best_weight = accumulated_weight
                best_path = path[:]
            return
 

        if len(path) >= max_vertices:
            return
 
        for neighbor in range(n):
            edge_weight = matrix[current][neighbor]
            if edge_weight != 0 and neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
 
                dfs(neighbor, path, accumulated_weight + edge_weight, visited)
 
                path.pop()
                visited.remove(neighbor)
 
    dfs(origin, [origin], 0, {origin})
 
    return best_weight, best_path
 
 
#  Saída formatada
def display_result(best_weight, best_path):
    if best_path is None:
        print("Não existe caminho válido.")
    else:
        path_str = " -> ".join(map(str, best_path))
        print(f"Caminho: {path_str}")
        print(f"Peso total: {best_weight}")
 
 
#  Ponto de entrada
def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "input/entrada.txt" or "/uploads/entrada.txt"
 
    try:
        n, matrix, origin, destination, max_vertices = read_input_file(file_path)
    except FileNotFoundError:
        print(f"Erro: arquivo '{file_path}' não encontrado.")
        sys.exit(1)
    except ValueError as e:
        print(f"Erro ao ler entrada: {e}")
        sys.exit(1)
 
    if not (0 <= origin < n) or not (0 <= destination < n):
        print("Erro: vértice de origem ou destino fora do intervalo válido.")
        sys.exit(1)
 
    if max_vertices < 2:
        print("Não existe caminho válido.")
        return
 
    best_weight, best_path = find_max_weight_path(
        n, matrix, origin, destination, max_vertices
    )
 
    display_result(best_weight, best_path)
 
 
if __name__ == "__main__":
    main()
