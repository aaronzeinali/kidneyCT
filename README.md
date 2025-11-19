
<header>
  <div>
    <h1>ct-kidney-dataset-cba <span class="badge">v1.0</span></h1>
    <div class="muted">A curated CT kidney image collection (Normal / Cyst / Tumor / Stone) for research & baseline experiments</div>
  </div>
</header>

<section class="section" id="summary">
  <h2>Summary</h2>
  <p>This repository hosts the <strong>ct-kidney-dataset-cba</strong>: a curated collection of axial CT kidney images organized into four clinical categories — <em>normal</em>, <em>cyst</em>, <em>tumor</em>, and <em>stone</em>. The dataset is intended for classification and basic detection/benchmarking tasks, and include
<header>
  <div>
    <h1>ct-kidney-dataset-cba <span class="badge">v1.0</span></h1>
    <div class="muted">A curated CT kidney image collection (Normal / Cyst / Tumor / Stone) with ROI-extracted processed images</div>
  </div>
</header>

<section class="section" id="summary">
  <h2>Summary</h2>
  <p>
    <strong>ct-kidney-dataset-cba</strong> is a structured dataset of kidney CT images categorized into
    <em>normal</em>, <em>cyst</em>, <em>tumor</em>, and <em>stone</em> classes.
    The dataset contains both raw slices and a new set of <strong>Region-of-Interest (ROI) extracted images</strong> created using a custom high-precision extraction pipeline and advanced enhancement technology developed specifically for this project.
  </p>
</section>

<section class="section" id="contents">
  <h2>Repository Contents</h2>
  <table>
    <thead><tr><th>Path</th><th>Description</th></tr></thead>
    <tbody>
      <tr><td><code>/data/images/normal/</code></td><td>Original CT slices labeled <code>normal</code></td></tr>
      <tr><td><code>/data/images/cyst/</code></td><td>Original CT slices showing renal cysts</td></tr>
      <tr><td><code>/data/images/tumor/</code></td><td>Original CT slices showing renal tumors</td></tr>
      <tr><td><code>/data/images/stone/</code></td><td>Original CT slices showing stones</td></tr>

      <tr><td><code>/processed_images/</code></td>
          <td><strong>NEW:</strong> ROI-extracted images using enhanced processing & precision-region extraction (details below)</td>
      </tr>

      <tr><td><code>/metadata/labels.csv</code></td><td>Metadata manifest (<code>filename, label, patient_id, series_id, notes</code>)</td></tr>
      <tr><td><code>/notebooks/</code></td><td>Jupyter notebooks for loading, visualization, preprocessing & baseline models</td></tr>
      <tr><td><code>/LICENSE</code></td><td>Dataset license</td></tr>
    </tbody>
  </table>
</section>

<section class="section" id="processed-images">
  <h2>Processed Images (ROI Extraction)</h2>

  <p>
    The <strong>processed_images</strong> directory contains a refined version of the dataset where each CT slice has been passed through a custom high-accuracy ROI extraction and enhancement pipeline.
  </p>

  <h3>What’s inside <code>/processed_images/</code></h3>
  <ul>
    <li>Precise kidney/lesion ROI extraction around the dominant region of interest</li>
    <li>Advanced windowing & contrast optimization</li>
    <li>Artifact-reduced and noise-suppressed slices</li>
    <li>Uniform dimensions for ML pipelines</li>
    <li>One-to-one mapping with the original filenames for easy alignment</li>
  </ul>

  <h3>Folder Structure</h3>
  <pre><code>/processed_images/
    ├── normal/
    ├── cyst/
    ├── tumor/
    └── stone/
  </code></pre>

  <h3>Highlights of the New Method</h3>
  <ul>
    <li><strong>Automatic ROI detection</strong> using hybrid intensity-based + geometric filtering</li>
    <li><strong>Super-resolution enhancement</strong> for improved detail visibility</li>
    <li><strong>Noise smoothing</strong> while preserving diagnostic texture</li>
    <li><strong>Adaptive cropping</strong> that maintains the lesion context</li>
    <li><strong>Consistent output size</strong> for deep learning pipelines (no rescaling artifacts)</li>
  </ul>

  <div class="note">
    These ROI-extracted images offer a cleaner, more model-friendly dataset and are recommended for training classification models, while the original images are ideal for validation, clinical comparison, or segmentation tasks.
  </div>
</section>

<section class="section" id="download">
  <h2>Download</h2>
  <p>
    Download the dataset or load it programmatically:
  </p>
  <pre><code>wget -O ct-kidney-dataset-cba.zip "<YOUR_DOWNLOAD_LINK>"
unzip ct-kidney-dataset-cba.zip -d ./data/
</code></pre>
</section>

<section class="section" id="usage">
  <h2>Quick Usage (Python)</h2>
  <p>Load both original & ROI-extracted images:</p>
  <pre><code>import pandas as pd
from PIL import Image

df = pd.read_csv("metadata/labels.csv")
row = df.iloc[0]

orig = Image.open(f"data/images/{row.label}/{row.filename}")
roi  = Image.open(f"processed_images/{row.label}/{row.filename}")

orig.show()
roi.show()
</code></pre>
</section>

<section class="section" id="baseline">
  <h2>Baseline Training Recipe</h2>
  <ul>
    <li>Resize all images to 224×224 or model’s native input</li>
    <li>Use ROI images for training for higher consistency</li>
    <li>Use the original images for robustness validation</li>
  </ul>
</section>

<section class="section" id="ethics">
  <h2>Ethics & Privacy</h2>
  <p>All data was anonymized and stripped of identifying metadata before release.</p>
</section>

<section class="section" id="citation">
  <h2>Citation</h2>
  <pre><code>@misc{ct-kidney-dataset-cba-2025,
  title = {ct-kidney-dataset-cba: CT Kidney Dataset with ROI Extraction},
  author = {Your Name},
  year = {2025},
  howpublished = {GitHub repository},
  url = {https://github.com/<your-org>/ct-kidney-dataset-cba}
}
</code></pre>
</section>

<section class="section" id="license">
  <h2>License</h2>
  <p>Dataset License: <strong>&lt;YOUR_LICENSE&gt;</strong></p>
</section>

<footer class="small muted" style="margin-top:18px">
  Maintainer: <strong>Your Name</strong> — contact: <a href="mailto:you@example.com">you@example.com</a>
</footer>
