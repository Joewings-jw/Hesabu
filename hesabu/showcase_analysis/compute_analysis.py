import requests
import io
from PIL import Image

def analyze_math_solution(image_file):
  """Analyzes a math solution from Bard API by uploading an image of a solved math problem and returning LaTeX.

  Args:
    image_file: A file object containing the image of the solved math problem.

  Returns:
    A string containing the LaTeX for the solved math problem.
  """

  # Prepare the image file.
  image = Image.open(image_file)
  image_bytes = io.BytesIO()
  image.save(image_bytes, format="PNG")

  response = requests.post(
      "https://api.bard.ai/analyze_math_solution",
      files={"image": image_bytes},
      headers={"Authorization": "API_KEY"},
  )

  if response.status_code != 200:
    raise Exception("Failed to analyze math solution: {}".format(response.content))

  latex = response.json()["latex"]

  return latex

def sanitize_latex_for_optimization(latex):
  """Sanitizes the returned LaTeX for optimization.

  Args:
    latex: A string containing the LaTeX for the solved math problem.

  Returns:
    A string containing the sanitized LaTeX for the solved math problem.
  """

  latex = latex.replace(" ", "").replace("\n", "")

  # Replace certain characters with their LaTeX equivalents.
  latex = latex.replace(r"&", r"\&")
  latex = latex.replace(r"\%", r"\%")

  return latex


