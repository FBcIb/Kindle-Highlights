# Kindle-Highlights
Separate Kindle Highlights into Words (for definitions), Noted content, and Quotes.

# On windows, run from a batch file (if env is added to PATH)
Create a filename.bat file in your env and run with win+r  
Batch file should have:    
  call C:\Path\to\venv\Scripts\Activate  
  py C:\Path\to\file\highlight.py %*  
  pause  

# Future Functionality
-Autowrite to your own Google Drive in separate Doc files.
-Add definitions to highlighted words.
