from net import network


def main():
    net = network(inputs=10, hlayers=3, hneurons=6, outputs=3)
    print(net.propagate(inputs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

if __name__ == "__main__":
    main()
