import java.util.*;

class Edge {
    int destination;
    int weight;

    Edge(int destination, int weight) {
        this.destination = destination;
        this.weight = weight;
    }
}

public class DijkstraAlgorithm {

    public static void dijkstra(List<List<Edge>> graph, int source) {
        int n = graph.size();

        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);

        distance[source] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(
                Comparator.comparingInt(a -> a[1]));

        pq.offer(new int[]{source, 0});

        while (!pq.isEmpty()) {
            int[] current = pq.poll();

            int node = current[0];
            int dist = current[1];

            if (dist > distance[node]) {
                continue;
            }
