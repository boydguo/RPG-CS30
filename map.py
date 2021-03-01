import locations


# creates and prints out map
class Map:
    def __init__(self):
        self.position = 0
        self.map = [
            locations.DropSite(),
            locations.Blanc(),
            locations.Salem(),
            locations.Louisberg(),
            locations.Rennes(),
            locations.Rouan(),
            locations.Orleans(),
            locations.Bourges(),
            locations.Toulon(),
            locations.Vice(),
            locations.AlliedForces(),
        ]
        self.formatted_map = (
            "{:^13}                                                        \n"
            "     *     {:^13}                                             \n"
            "                 *            {:^13}                          \n"
            "                                    *                         \n"
            "                                             {:^13}           \n"
            "                                                   *          \n"
            "                                          {:^13}              \n"
            "                                                *             \n"
            "                                     {:^13}                   \n"
            "                                           *                  \n"
            "                      {:^13}                                  \n"
            "                            *                                 \n"
            "             {:^13}                                           \n"
            "                   *                                          \n"
            "                              {:^13}                          \n"
            "                                    *                         \n"
            "                                             {:^13}           \n"
            "                                                   *          \n"
            "                                 {:^13}                       \n"
            "                                       *                      \n"
        )

    def print(self):
        print(
            self.formatted_map.format(
                *(
                    f"[{x.name}]" if i == self.position else x.name
                    for i, x in enumerate(self.map)
                )
            )
        )

        tile = self.map[self.position]

        print(f"You are currently at {tile.name}")
        print(f"It is {tile.info}")
