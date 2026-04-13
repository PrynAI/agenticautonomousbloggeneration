from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState

class Graph_Builder:
    def __init__(self, llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)
    
    def build_topic_graph(self):
        """
        Build a grpah to generate blogs based on topic
        """
        #Nodes
        self.graph.add_node("title_creation",)
        self.graph.add_node("content_generation",)

        #Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_Generation")
        self.graph.add_edge("content_generation",END)

        return self.graph






        
