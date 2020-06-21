import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
//this class implements breathFirstSearch(BFS) algorithm on a binary
//data structure given in Array format
public class BFS
{
    public static void main(String[] args)
    {
        int[][] edges = {{1,2},{1,3},{2,4},{2,5}};
        System.out.println(bfs(10, 4, edges, 1));
    }

    private static Queue<Integer> queue = new LinkedList<>();
    private static Integer currentNode;
    private static ArrayList<Integer> Visited = new ArrayList<>();
    private static int cost = 6; private static ArrayList<Integer> Costs = new ArrayList<>();

    static ArrayList<Integer> bfs(int n, int m, int[][] edges, int s)
    {
        queue.add(s); Visited.add(currentNode);//
        while (!queue.isEmpty())
        {
            currentNode = queue.element(); queue.remove();//get the first element in queue and remove it
            ArrayList<Integer> adjacents = search(edges,currentNode);
            for (int node : adjacents)
            {
                if(!Visited.contains(node))
                {
                    Visited.add(node); queue.add(node);
                    Costs.add(cost);
                }
            }
            cost += 6;
        }
        if(Costs.size() <= n-2)//not all nodes are connected
        {
            while(Costs.size()<= n-2) Costs.add(-1);
        }
        return Costs;
    }
    static ArrayList<Integer> search(int[][] edges, int currentNode)
    {//searches nodes connected to current edge
        ArrayList<Integer> adjacents = new ArrayList<>();
        for (int i=0;i<edges.length;i++)
        {//loop through array of edges and find the cost from start node
            if(edges[i][0]==currentNode)
            {//if edge has currentNode
                adjacents.add(edges[i][1]);
            }
        }
        return adjacents;
    }

}
