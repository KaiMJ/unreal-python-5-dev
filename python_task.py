"""Task:

Design a high level class that handles the scene graph generation.

Assume call_llm is already implemented. 

Note that we can use json_schema to force the LLM to always output in JSON in OpenAI style.
"""

def call_llm(text, json_schema):
    text = "“Create a driving scene with an intersection at a red light."
    json_schema = {
        "type": "object",
        "properties": {
            "intersection_light": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "array",
                        "items": {
                            "type": "number"
                        },
                        "description": "Location in X,Y,Z..."
                    },
                    "scale": {
                        "type": "array",
                        "items": {
                            "type": "number"
                        },
                        "description": "Scale in W,H,C..."
                    },
                    "color": {
                        "type": "string",
                        "description": "Color of the intersection light"
                    }
                },
                "required": ["location", "scale", "color"]
            },
            "street": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "array",
                        "items": {
                            "type": "number"
                        },
                        "description": "Location in X,Y,Z..."
                    },
                    "scale": {
                        "type": "array",
                        "items": {
                            "type": "number"
                        },
                        "description": "Scale in W,H,C..."
                    },
                    "color": {
                        "type": "string",
                        "description": "Color of the street"
                    }
                },
                "required": ["location", "scale", "color"]
            }
        },
        "required": ["intersection_light", "street"]
    }

    return


class API:
    def generate(self, prompt, strict=False):
        scene_graph = SceneGraph()
        scene_graph.generate(prompt, strict)
        return scene_graph

class SceneGraph:
    def __init__(self):
        self.scene_graph = None

    def generate(self, prompt, strict=False):
        if self.scene_graph is None:
            json_graph = call_llm(prompt, json_schema=None)
            self.scene_graph = json_graph
        else:
            combined_prompt = prompt + self.scene_graph
            json_graph = call_llm(combined_prompt, json_schema=None)
            self.scene_graph = json_graph

        return json_graph
