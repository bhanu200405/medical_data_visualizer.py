from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

def main():
    # Draw and save the categorical plot
    cat_fig = draw_cat_plot()
    cat_fig.savefig("catplot.png")
    print("Categorical plot saved as catplot.png")
    
    # Draw and save the heatmap
    heat_fig = draw_heat_map()
    heat_fig.savefig("heatmap.png")
    print("Heatmap saved as heatmap.png")
    
    # Optional: show the plots interactively
    # plt.show()  # Uncomment this line if you want to see the plots immediately

if __name__ == "__main__":
    main()
