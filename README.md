# Brain Tumor Detection using Deep Learning

A deep learning project for automated brain tumor detection and classification from MRI images using EfficientNetB0 architecture.

## 🎯 Project Overview

This project implements a convolutional neural network (CNN) based approach to detect and classify brain tumors from MRI scans. The model can classify images into four categories:
- **Glioma** - A type of brain and spinal cord tumor
- **Meningioma** - A tumor of the membrane surrounding the brain
- **Pituitary** - A tumor of the pituitary gland
- **No Tumor** - Normal, healthy brain scans

## 📋 Features

- ✅ Deep learning model using EfficientNetB0 pre-trained architecture
- ✅ Data augmentation and preprocessing
- ✅ Model training and evaluation pipeline
- ✅ Data visualization and analysis
- ✅ Flask-based web application for predictions
- ✅ Support for MRI image batch processing

## 🔧 Requirements

- Python 3.7+
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Pillow (PIL)
- Flask (for web app)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Muhammad-Ali5/Brain-tumor-Detection-using-DL.git
   cd Brain-tumor-Detection-using-DL
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download/Prepare dataset**
   - The MRI images dataset should be organized in the following structure:
   ```
   MRI images/
   ├── Training/
   │   ├── glioma/
   │   ├── meningioma/
   │   ├── notumor/
   │   ├── pituitary/
   │   └── yes/
   └── Testing/
       ├── glioma/
       ├── meningioma/
       ├── notumor/
       └── pituitary/
   ```

## 🚀 Usage

### Training the Model

Run the training notebook:
```bash
jupyter notebook Brain_tumor.ipynb
```

### Data Visualization

Analyze the dataset:
```bash
jupyter notebook data_visualization.ipynb
```

### Classification with EfficientNetB0

Advanced training and evaluation:
```bash
jupyter notebook brain-tumor-classification-with-efficientnetb0.ipynb
```

### Web Application

Run the Flask application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📊 Project Structure

```
Brain-tumor-Detection-using-DL/
├── app.py                                      # Flask web application
├── Brain_tumor.ipynb                           # Main training notebook
├── brain-tumor-classification-with-efficientnetb0.ipynb  # Advanced notebook
├── data_visualization.ipynb                    # Data analysis notebook
├── Untitled.ipynb                              # Additional analysis
├── MRI images/                                 # Dataset directory
│   ├── Training/
│   │   ├── glioma/
│   │   ├── meningioma/
│   │   ├── notumor/
│   │   ├── pituitary/
│   │   └── yes/
│   └── Testing/
│       ├── glioma/
│       ├── meningioma/
│       ├── notumor/
│       └── pituitary/
├── requirements.txt                            # Python dependencies
├── .gitignore                                  # Git ignore file
└── README.md                                   # This file
```

## 🧠 Model Architecture

The project uses **EfficientNetB0**, a state-of-the-art CNN architecture that:
- Provides excellent accuracy with relatively small model size
- Uses transfer learning from ImageNet pre-trained weights
- Employs compound scaling of depth, width, and resolution
- Achieves competitive performance on image classification tasks

## 📈 Model Performance

*Add your model's performance metrics here after training:*
- Training Accuracy: XX%
- Validation Accuracy: XX%
- Test Accuracy: XX%
- Precision: XX%
- Recall: XX%
- F1-Score: XX%

## 🔍 Key Techniques Used

- **Transfer Learning**: Pre-trained EfficientNetB0 on ImageNet
- **Data Augmentation**: Rotation, flip, zoom, and brightness adjustments
- **Regularization**: Dropout and batch normalization
- **Class Imbalance Handling**: Class weights and sampling strategies
- **Image Preprocessing**: Normalization and resizing

## 📝 Dataset Information

The dataset contains MRI brain scans classified into tumor and non-tumor categories with further subcategories for tumor types.

**Dataset Statistics:**
- Total Images: ~7,000+
- Training Images: ~5,000+
- Testing Images: ~1,000+
- Image Size: Varies (standardized during preprocessing)
- Format: JPG/JPEG

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Muhammad Ali**
- GitHub: [@Muhammad-Ali5](https://github.com/Muhammad-Ali5)
- Email: maliuetm507@gmail.com

## 🙏 Acknowledgments

- TensorFlow/Keras team for the deep learning framework
- ImageNet dataset creators
- EfficientNet paper authors (Tan & Le, 2019)

## ⚠️ Disclaimer

This project is for educational and research purposes. The model should not be used for medical diagnosis without proper validation and approval from medical professionals. Always consult healthcare experts for medical decisions.

## 📞 Contact & Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Last Updated**: April 26, 2026
