def feature_extract(url):
    l = url.split(":")  # Split to get https status
    # features
    ssl_check = 0  # 0: https not present
    atTheRateCheck = 0  # 0: https not present
    dot_count = 0
    dash_check = 0
    len_host_name = 0  # binary
    slash_count = 0  # counter
    slash_check = 0  # check
    ip_present_check = 1

    l[1] = l[1][2:]  # remove "//" from the link

    # https check
    if l[0] == "https":
        ssl_check = 1

    for char in l[1]:
        # @ check
        if char == "@":
            if atTheRateCheck == 0:
                atTheRateCheck = 1
        # dot count
        elif char == ".":
            dot_count += 1
        elif char == "-":
            dash_check = 1
        elif char == "/":
            slash_count += 1

    if slash_count > 5:
        slash_check = 1

    l_host_list = l[1].split("/")

    for i in l_host_list[0]:
        if 48 <= ord(i) <= 57 or i == ".":
            continue
        else:
            ip_present_check = 0
            break

    # print(l_host_list)
    if len(l_host_list[0]) > 25:
        len_host_name = 1

    # print("ip_present_check", ip_present_check,"atTheRateCheck", atTheRateCheck, "ssl_check", ssl_check, "dot_count", dot_count, "dash_check", dash_check,
    # "len_host_name", len_host_name, "slash_check", slash_check)

    # print(ssl_check)
    # print(l)
    # 1: Phising
    # 0: Not Phising
    return [int(ssl_check), int(atTheRateCheck), int(ip_present_check), int(dot_count), int(slash_count),
            int(dash_check), int(len_host_name), int(slash_check),]


def main():
    url_list = []
    try:
        with open("raw_datasets/legitimate_urls.txt", "r") as f:
            lines = f.readlines()
            # print(len(lines))
            for line in lines:
                url_list.append(line.strip("\n"))
                # print(line)

    except FileNotFoundError:
        print("File Not Found!")
    # print(len(url_list))
    data_set_list = []

    # url = ""
    for url in url_list:
        url_details = feature_extract(url)
        data_set_list.append(url_details)

    print(len(data_set_list))
    print(data_set_list)
    # for url in url_list:
    # feature_extract(url)
    temp = None
    with open("ruba_phising_data_set_build_final.csv", "a") as f:
        for data_str in data_set_list:
            temp = ",".join(data_str)
            temp += "\n"
            f.write(temp)

    # print(url_list)
    print("Ruba")


if __name__ == '__main__':
    main()
