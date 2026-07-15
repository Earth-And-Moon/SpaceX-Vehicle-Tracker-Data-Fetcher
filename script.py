import requests, time
url = "https://sxcontent9668.azureedge.us/cms-assets/starship_tracker_public.json"
tgt = "data/data.txt"

run_every = 10.0	# sec	1
log_every = 600.0	# sec	3

run_for = 295		# end script after x sec	10


def do_it():
	text = ""
	try:
		t1 = time.time()
		code = -1
		headers = {}
		success = False
		error = []
		try:
			r = requests.get(url)
			code = r.status_code
			headers = str(r.headers).replace('"', "[quote]")
			success = True
		except Exception as e:
			error = str([str(type(e)), str(e.args), str(e)]).replace('"', "[quote]")
		t2 = time.time()
		data = r.text
		debug = "{" + f'''"time_1":{str(t1)},"time_2":{str(t2)},"status_code":{str(code)},"headers":"{str(headers)}","success":"{str(success)}","error":"{str(error)}"''' + "}"
		text += debug + "\n" + data
	except Exception as e:
		text += "Error: " + str(e) + " at " + str(time.time())

	return text

def log(data):
	with open(tgt, "a") as f:
		f.write(data + "\n")


def main():
	t = time.time()

	while time.time() < t + run_for:	#True:
		text = ""

		t_loop_start = time.time()

		while time.time() <= t_loop_start + log_every:
			print("run")
			text += do_it()
			text += "\n--\n"
			time.sleep(run_every)

		print("log")

		log(text)

main()








