# Examples

This folder contains various Manim scripts for creating animations. It showcases top-notch Manim code snippets and their corresponding video/image outputs, demonstrating various library functionalities. 
Dive into the world of Manim excellence! ✨🎥

## Collections


- [`moving_frame`](moving_frame/): Explore animations related to moving frames. [Watch Animation.](moving_frame/media/videos/moving_frame_box/480p15/moving_frame.gif)
- [`sine_curve`](sine_curve/): Check out animations illustrating sine curves. [Watch Animation.](sine_curve/media/videos/sine_surve_animation/480p15/SineCurveUnitCircle.gif)
- [`ThreeDCameraIllusionRotation`](three_d/): Explore an illusionary rotation of a 3D scene. [Watch Animation.](three_d/media/videos/three_d_rotation/480p15//ThreeDCameraIllusionRotation.gif)


## Usage

To run a animation script, navigate to the respective folder and use the following command:

You could try editting the script or delete the media folder with

```bash
rm -rf media/
```

Then to regenerate the animation, run:

```bash
manim -p -ql script_name.py SceneClassName
```

- `-p`: Flag for preview mode.
- `-ql`: Flag for "quality low" (optional, for faster previews).

## Example

Let's run an example from the `sine_curve` folder:

```bash
manim -p sine_curve/sine_surve_animation.py SineCurveUnitCircle
```
