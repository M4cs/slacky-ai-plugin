import gpt_2_simple as gpt2

run_name='slack_export_dataset.txt'
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name=run_name)

def generate_res(text):
    generation = str(gpt2.generate(sess, run_name=run_name, return_as_list=True, temperature=0.5, nsamples=20, batch_size=20, length=150, prefix="max\nhey I found a bug on the lender side, could you take a look at it?")[0])
    return generation