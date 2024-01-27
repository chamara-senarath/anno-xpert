# AnnoXpert - A Query Interface to Machine-readable Documents

This is a software tool designed to facilitate the querying of machine-readable documents. With this application, you can effortlessly upload XML files and corresponding schema files (.xsd) to the application, enabling you to interactively search and extract information from documents. 

The software provides both a desktop and web application for your ease of use. Kindly be aware that the demo link for the web application hosted online is intended solely for demonstration purposes. Please refrain from uploading sensitive documents or attempting to process a large number of documents through this demo link, as it is designed exclusively for demonstration. For actual use, please use the desktop version on your computer or run the web application locally.

### How to Use video - [ Link ](https://drive.google.com/file/d/18ms9-oVV1GTxKlH_27dCNbviqCZ7hLft/view?usp=drive_link)

### View online Demo - [https://query-interface.netlify.app](https://query-interface.netlify.app/)

## Features

### 1. Schema-driven Querying

The application simplifies the querying process by allowing you to upload a schema file associated with your XML document. Once uploaded, the application generates dropdown menus populated with schema-defined options, making it easy to construct precise queries.

### 2. Flexible Search Options

The software provides a versatile search interface that includes a search box, case-sensitive option, and the ability to adjust the approximate string matching level. These features empower you to fine-tune your queries according to your specific requirements.

### 3. Document Filtering

The application includes filtering capabilities, allowing you to refine your search results further. You can apply filters based on specific criteria to extract only the information you need.


## Running the Desktop Application

To run the desktop application, follow these steps:

1. Ensure Python is installed on your computer.
2. Install the required Python packages by running the following command:

   ```shell
   pip install ttkbootstrap lxml fuzzyset bigtree
   ```

3. Navigate to the parent folder and execute the following command to start the application:

   ```shell
   python main.py
   ```

## Running the Web Application

To run the web application, follow these steps:

1. Make sure you have Node.js and npm installed on your computer.
2. Navigate to the "web" folder, which contains both the API and frontend components.
3. Navigate to "api" folder and install FastAPI by running the following command:

   ```shell
   pip install fastapi
   ```

4. You will also need an ASGI server, such as Uvicorn. To install Uvicorn, run:

   ```shell
   pip install "uvicorn[standard]"
   ```

5. Start the API server using the following command from the "api" folder:

   ```shell
   uvicorn main:app --reload
   ```

6. Move to the "frontend" folder within "web" and install all the required packages:

   ```shell
   npm install
   ```

7. Launch the frontend using:

   ```shell
   npm run dev
   ```

You can now access the application frontend via http://localhost:5173.
