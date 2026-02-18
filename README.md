# CIFAR-10 Image Classifier

A deep learning web application that classifies images into 10 categories using a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset.

## 🎯 Features

- **Image Classification**: Upload any image and get instant predictions across 10 categories
- **Real-time Predictions**: Fast inference using a trained CNN model
- **User-friendly Interface**: Simple and intuitive web interface
- **RESTful API**: FastAPI backend for easy integration
- **Custom Model Training**: Includes training scripts to retrain or fine-tune the model

## 📋 Categories

The classifier can identify the following 10 classes:
- ✈️ Airplane
- 🚗 Automobile
- 🐦 Bird
- 🐱 Cat
- 🦌 Deer
- 🐕 Dog
- 🐸 Frog
- 🐴 Horse
- 🚢 Ship
- 🚚 Truck

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **TensorFlow/Keras**: Deep learning framework for model training and inference
- **Uvicorn**: ASGI server for FastAPI
- **Pillow**: Image processing library
- **NumPy**: Numerical computing library

### Frontend
- **HTML5/CSS3**: Modern web technologies
- **JavaScript**: Client-side functionality
- **Responsive Design**: Works on desktop and mobile devices

## 📁 Project Structure

```
cifar10-image-classifier/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application
│   │   ├── model_loader.py      # Model loading utilities
│   │   └── predict.py           # Prediction endpoint
│   ├── model/
│   │   └── cifar10_model.h5     # Trained model file
│   └── requirements.txt         # Python dependencies
│
├── frontend/
│   ├── index.html               # Main web page
│   ├── script.js                # Client-side logic
│   └── style.css                # Styling
│
├── training/
│   ├── train.py                 # Model training script
│   ├── data_utils.py            # Data loading utilities
│   ├── evaluate.py              # Model evaluation script
│   └── saved_model/
│       └── cifar10_model.h5     # Saved trained model
│
└── README.md                    # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cifar10-image-classifier.git
   cd cifar10-image-classifier
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Application

1. **Start the FastAPI backend**
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`

2. **Open the frontend**
   - Open `frontend/index.html` in your web browser
   - Or use a local server:
     ```bash
     cd frontend
     python -m http.server 8080
     ```
   - Navigate to `http://localhost:8080`

3. **Make Predictions**
   - Click "Choose Image" to upload an image
   - Click "Predict" to get the classification result
   - View the predicted class and confidence score

### API Documentation

Once the backend is running, visit:
- **Interactive API Docs**: `http://localhost:8000/docs`
- **Alternative Docs**: `http://localhost:8000/redoc`

### API Endpoint

**POST** `/predict`
- **Description**: Classify an uploaded image
- **Request**: Multipart form data with image file
- **Response**: 
  ```json
  {
    "class": "airplane",
    "confidence": 0.95
  }
  ```

## 🎓 Model Architecture

The CNN model consists of:
- **Input Layer**: 32×32×3 RGB images
- **Convolutional Layers**: 3 Conv2D layers (32, 64, 128 filters)
- **Pooling Layers**: MaxPooling2D after each convolution
- **Dense Layers**: 256-unit fully connected layer
- **Dropout**: 0.5 dropout rate for regularization
- **Output Layer**: 10-unit softmax layer

### Model Training

To train the model from scratch:

```bash
cd training
python train.py
```

The training script will:
1. Load the CIFAR-10 dataset automatically
2. Train the CNN model for 10 epochs
3. Save the trained model to `saved_model/cifar10_model.h5`

### Model Evaluation

To evaluate the model performance:

```bash
cd training
python evaluate.py
```

## 📊 Performance

- **Dataset**: CIFAR-10 (60,000 32×32 color images)
- **Training Images**: 50,000
- **Test Images**: 10,000
- **Model Size**: ~5MB
- **Expected Accuracy**: ~70-75% on test data

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Report bugs and issues
2. Suggest new features or enhancements
3. Improve documentation
4. Submit pull requests

### Steps to Contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **CIFAR-10 Dataset**: [Learning Multiple Layers of Features from Tiny Images](https://www.cs.toronto.edu/~kriz/cifar.html) by Alex Krizhevsky
- **TensorFlow/Keras**: For the deep learning framework
- **FastAPI**: For the modern web framework

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This model is trained on the CIFAR-10 dataset which contains small 32×32 pixel images. For best results, upload clear, centered images of the objects you want to classify.
