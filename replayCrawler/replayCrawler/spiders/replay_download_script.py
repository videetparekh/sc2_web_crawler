import os
import csv
import urllib2


def downloader(download_url):
    replay_name = "ggtracker_" + (download_url.split("/")[-2])
    file_name = replay_name + ".SC2Replay"
    folder_path = "%%%%%PATH%%%%%" + replay_name    # Replace placeholder with the location in which the files should be stored
    file_path = folder_path + "/" + file_name

    get_file = urllib2.urlopen(download_url)
    file_data = get_file.read()

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(file_path, 'wb') as f:
        f.write(file_data)


def read_download_urls():
    file_path = "%%%%%PATH%%%%%"    # Requires the file path for the CSV with the file links
    file_store = []
    file = open(file_path, 'r+')
    for line in csv.reader(file):
        file_store.append(line)
    return file_store


download_urls = [ele[0] for ele in read_download_urls() if ele != ['']]
download_urls = list(set(download_urls))
start_bound = int(raw_input("Start Bound: "))
end_bound = start_bound + int(raw_input("Download Limit: "))

for url in download_urls[start_bound:end_bound]:
    if url != '':
        print "Downloading replay ", download_urls.index(url)+1, " of ", len(download_urls)
        try:
            downloader(url)
        except:
            print "Failed."
    else:
        continue
