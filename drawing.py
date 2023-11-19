def start_drawing(event)
    global is_drawing, prev_x, prev_y
    is_drawing=True
    prev_x, prev_y=event.x,event.y

def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x,current_y =event.x, event.y
        canvas.create_line(prev_x,prev_y,current_x, current_y,fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y= current_x, current_y

        def stop_drawing(event):
            global is_drawing
            is_drawing =False

            def change_pen_color():
                global drawing_color
                color=askcolor()[1]
                if color:
                    drawing_color=color

                        global line_width
                        line_width = int(value)